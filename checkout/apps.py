from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Import used for its side effects (signal registration),
        not directly referenced.
        noqa is added to avoid false positive linting warnings.
        """
        import checkout.signals  # noqa: F401
