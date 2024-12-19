from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, password, **extra_fields)

class Plan(models.Model):
  stripe_price_id = models.CharField(max_length=255, null=True)
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  price_per_hook = models.DecimalField(
    max_digits=5, decimal_places=2, null=True
  )
  hook_limit = models.IntegerField(default=0)

class StripeCustomer(models.Model):
  user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
  stripe_customer_id = models.CharField(max_length=255)

class Subscription(models.Model):
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
  stripe_subscription_id = models.CharField(max_length=255, null=True)
  customer = models.ForeignKey(
    StripeCustomer, on_delete=models.CASCADE, null=True
  )
  hooks = models.IntegerField(default=0)
  merge_credits = models.IntegerField(blank=True, null=True)
  current_period_end = models.IntegerField(default=0)

class User(AbstractUser):
  email = models.EmailField(unique=True, null=False, blank=False)
  api_key = models.CharField(max_length=255, blank=True, null=True)
  verification_token = models.CharField(max_length=100, blank=True, null=True)
  subscription = models.ForeignKey(
    Subscription, on_delete=models.SET_NULL, null=True
  )

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def save(self, *args, **kwargs):
    self.username = self.email
    super().save(*args, **kwargs)

  def can_generate_video(self):
    return self.subscription.hooks >= 1
