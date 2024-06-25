import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "case_study.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import case_study.users.signals  # noqa: F401
