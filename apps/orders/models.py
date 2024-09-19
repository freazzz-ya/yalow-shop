from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

from apps.constants import Constants, HelpText
from apps.users.models import ClientUser


class BaseModel(models.Model):
    """BaseModel"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractCategories(BaseModel):
    """Model for Categories"""

    title = models.CharField(
        verbose_name=_('title'),
        max_length=Constants.CHARFIELD,
        unique=True,
        help_text=_(f'{HelpText.CATEGORIES_TITLE}')
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=Constants.TEXTFIELD,
        help_text=_(f'{HelpText.CATEGORIES_DESCRIPTION}')
    )

    class Meta:
        db_table = 'categories'
        verbose_name = _('categories')
        abstract = True

    def __str__(self) -> str:
        return f'{self.title}'


class Categories(AbstractCategories):
    """Model for Categories"""

    title = models.CharField(
        verbose_name=_('title'),
        max_length=Constants.CHARFIELD,
        unique=True,
        help_text=_(f'{HelpText.CATEGORIES_TITLE}')
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=Constants.TEXTFIELD,
        help_text=_(f'{HelpText.CATEGORIES_DESCRIPTION}')
    )

    class Meta:
        db_table = 'categories'
        verbose_name = _('categories')

    def __str__(self) -> str:
        return f'{self.title}'


class SubCategories(AbstractCategories):
    """Model for subcategories."""
    
    categories = models.ForeignKey(
        to=Categories,
        verbose_name=_('subcategories'),
        related_name='sub_categories',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'subcategories'
        verbose_name = _('subcategories')


class Product(BaseModel):
    """Class for product."""

    title = models.CharField(
        verbose_name=_('title'),
        max_length=Constants.CHARFIELD,
        unique=True,
    )
    image = models.ImageField(
        upload_to='images/product',
        verbose_name=_('image'),
    )
    article = models.CharField(
        verbose_name=_('article'),
        max_length=Constants.CHARFIELD,
    )
    categories = models.ForeignKey(
        to=Categories,
        verbose_name=_('subcategories'),
        related_name='category_products',
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        verbose_name=_('description'),
        max_length=Constants.TEXTFIELD,
    )
    author = models.ForeignKey(
        to=ClientUser,
        verbose_name=_("author"),
        related_name="products",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Resize the image
        img = img.resize((500, 610))

        # Set the image resolution
        img.info['dpi'] = (72, 72)

        # Set the image color depth
        img = img.convert('RGB')

        # Save the image as PNG
        img.save(self.image.path, 'PNG')

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        db_table = 'products'
        verbose_name = _('products')


class PurchasedProducts(BaseModel):
    """Model For Purchased Products."""

    product = models.ForeignKey(
        to=Product,
        verbose_name=_("PurchasedProduct"),
        on_delete=models.CASCADE,
        related_name='purchased_products',
    )
    platform_for_sale = models.TextField(
        verbose_name=_("platform for sale"),
        max_length=Constants.TEXTFIELD,
        help_text=_('Max symbols 1000'),
    )
    amount_products = models.IntegerField(
        verbose_name=_('amount products'),
        validators=[
            MinValueValidator(
                limit_value=Constants.INT_FIELD_MIN_VALUE,
                message=f'Min symbols '
                        f'{Constants.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=Constants.INT_FIELD_MAX_VALUE,
                message=f'Max symbols '
                        f'{Constants.INT_FIELD_MAX_VALUE}',
                )
        ],
        default=0,
    )
    damaged_products = models.IntegerField(
        verbose_name=_('amount damage products'),
        validators=[
            MinValueValidator(
                limit_value=Constants.INT_FIELD_MIN_VALUE,
                message=f'Min symbols '
                        f'{Constants.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=Constants.INT_FIELD_MAX_VALUE,
                message=f'Max symbols '
                        f'{Constants.INT_FIELD_MAX_VALUE}',
                )
        ],
        default=0,
    )

    @property
    def amount(self):
        return f'{self.amount_products * self.damaged_products}'

    class Meta:
        db_table = 'purchased_products'
        verbose_name = _('purchased_products')


class ExpectedPurchases(BaseModel):
    """Model for expected purchases"""

    product = models.ForeignKey(
        to=Product,
        verbose_name=_("Purchased Product"),
        on_delete=models.CASCADE,
        related_name='expected_products',
    )
    amount_products = models.IntegerField(
        verbose_name=_('amount products'),
        validators=[
            MinValueValidator(
                limit_value=Constants.INT_FIELD_MIN_VALUE,
                message=f'Min symbols '
                        f'{Constants.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=Constants.INT_FIELD_MAX_VALUE,
                message=f'Max symbols '
                        f'{Constants.INT_FIELD_MAX_VALUE}',
                    )
        ],
        default=0,
    )

    class Meta:
        db_table = 'expected_products'
        verbose_name = _('expected_products')


class MailingEmail(BaseModel):
    """model for mailing email."""

    email = models.EmailField(
        verbose_name=_('email'),
        unique=True,
        validators=[EmailValidator(
            message="Not correct email"
            )
        ]
    )

    class Meta:
        db_table = 'mailing_email'
        verbose_name = _("mailing email")
