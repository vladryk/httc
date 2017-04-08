from django.db import models
from django.utils.translation import ugettext_lazy as _

from markedskraft.models import Contract


NEW = 'new'
PENDING = 'pending'
CONFIRMED = 'confirmed'
CANCELED = 'canceled'
ORDER_STATUSES = (
    (NEW, _('New')),
    (PENDING, _('Pending')),
    (CONFIRMED, _('Confirmed')),
    (CANCELED, _('Canceled')),
)
BUY = 'B'
SELL = 'S'
ACTION_TYPE = (
    (BUY, 'B'),
    (SELL, 'S')
)


class Order(models.Model):
    order_id = models.IntegerField(unique=True, blank=True, null=True)
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUSES, default=NEW
    )
    action_type = models.CharField(
        max_length=1, choices=ACTION_TYPE, verbose_name=_('B/S')
    )

    contract = models.CharField(max_length=6, verbose_name=_('Ctrct'))
    quantity = models.IntegerField(verbose_name=_('Qty'))

    price = models.IntegerField(verbose_name=_('Prc'))

    mk_contract = models.ForeignKey(
        Contract, related_name='httc_orders', verbose_name=_('Markedskraft '
                                                             'contract')
    )
