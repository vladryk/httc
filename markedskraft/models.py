from django.db import models


class Contract(models.Model):
    contract_id = models.IntegerField(db_index=True)
    da_price = models.IntegerField(blank=True, null=True)
    VWAID = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = (('start_time', 'end_time'),)


class Order(models.Model):
    order_id = models.IntegerField()
    qty = models.IntegerField()
    contract = models.ForeignKey(Contract)

    class Meta:
        unique_together = (('order_id', 'revisions_nr'),)


class Trade(models.Model):
    from httc.models import Order as HttcOrder

    order_id = models.IntegerField(blank=True, null=True, db_index=True)
    httc_order_id = models.ForeignKey(HttcOrder, blank=True, null=True, db_index=True)
    trade_id = models.IntegerField(db_index=True)
    qty = models.IntegerField()
    contract = models.ForeignKey(Contract)
