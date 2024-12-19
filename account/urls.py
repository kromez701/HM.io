from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
  path("", home, name="home"),
  path("stage/", stage, name="stage"),
  path("login/", login_view, name="login"),
  path("logout/", logout_user, name="logout"),
  path('register/', register, name='register'),
  path('subscription/', subscription, name='subscription'),
  path('verify/<str:token>', verify, name='verify'),
  path('subscribe/<str:price_id>', subscribe, name='subscribe'),
  path('stripe-webhook', stripe_webhook, name='stripe_webhook'),
  path('manage-subscription', manage_subscription, name='manage_subscription'),
  path('billing-portal', billing_portal, name='billing_portal'),
  path('add-credits/<str:kind>', add_credits, name='add_credits'),
  path('add-credits-success', add_credits_success, name='add_credits_success'),
  path('add-credits-cancel', add_credits_cancel, name='add_credits_cancel'),
  path(
    'upgrade-subscription/<str:price_id>',
    upgrade_subscription,
    name='upgrade_subscription'
  ),
  path(
    'downgrade-subscription',
    downgrade_subscription,
    name='downgrade_subscription'
  ),
  path('cancel-subscription', cancel_subscription, name='cancel_subscription'),
  path(
    'terms-and-conditions', terms_and_conditions, name='terms_and_conditions'
  ),
  path('privacy-policy', privacy_policy, name='privacy_policy'),
  path('refund-policy', refund_policy, name='refund_policy'),
  path('affiliate-program', affiliate_program, name='affiliate_program'),
]
