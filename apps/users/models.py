from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.constants import UserModelConstant


class ClientUser(AbstractUser):
    """Model for users."""

    class Role(models.TextChoices):
        Admin = 'Admin', 'Admin role',
        special = 'Special', 'Special role',
        custom = 'Custom', 'Custom role',
        superuser = 'SuperUser', 'SuperUser role',

    telegram_id = models.PositiveBigIntegerField(
        blank=True,
        null=True,
        unique=True,
        verbose_name=_('telegram id'),
        error_messages={
            "unique": _('A user with that telegram id already exists.'),
        },
    )
    description_for_profil = models.TextField(
        verbose_name=_('description'),
        max_length=UserModelConstant.TEXTFIELD,
        default=UserModelConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
    )
    image = models.ImageField(
        upload_to='images/profile',
        verbose_name=_('image'),
        default='images/profile/nou.jpg',
    )
    role = models.CharField(
        max_length=UserModelConstant.CHARFIELD,
        choices=Role.choices,
        default=Role.custom,
    )

    class Meta:
        db_table = _('users')
        verbose_name = _('users')
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.username}'
