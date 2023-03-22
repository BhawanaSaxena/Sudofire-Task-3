from .models import Company
from allauth.account.signals import user_signed_up

from django.dispatch import receiver

@receiver(user_signed_up)
def create_user(sender,request,user,**kwargs):
    Company.objects.create(user=user)