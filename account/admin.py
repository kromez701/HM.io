from django.contrib import admin
from .models import *

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(StripeCustomer)
admin.site.register(User)
