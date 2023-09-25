from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class BookStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_store'

    def ready(self):
        logger.debug('book_store.apps.UsersConfig.ready')
        from book_store.signals import handlers
