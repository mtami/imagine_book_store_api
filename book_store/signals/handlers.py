from django.db.models.signals import post_save
from django.dispatch import receiver
from book_store.models.cart_model import Cart
from allauth.account.signals import user_signed_up
from django.conf import settings
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


@receiver(user_signed_up, sender=User)
def create_cart_for_new_user(request, user, **kwargs):
    logger.debug("new user sing-up!")
    Cart.objects.create(user=user)

