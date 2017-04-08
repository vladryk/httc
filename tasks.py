from django.db.models import Count
from utils import *
from httc.models import Order as HttcOrder


# 1st query
ce(
    '''SELECT *
       FROM httc_order
       WHERE mk_contract_id = 1000
       ORDER BY price''')

t(HttcOrder.objects.filter(mk_contract=1000).order_by('price'))

t(HttcOrder.objects.raw(
                        '''SELECT *
                           FROM httc_order
                           WHERE mk_contract_id = 1000
                           ORDER BY price'''))


# 2st query
ce(
    '''SELECT httc_order.id
       FROM httc_order
       WHERE mk_contract_id = 1000''')

t(HttcOrder.objects.filter(mk_contract=1000).values('id'))

t(HttcOrder.objects.raw(
                        '''SELECT `httc_order`.`id`
                           FROM `httc_order`
                           WHERE `httc_order`.`mk_contract_id` = 1000'''))


# 3st query
t(HttcOrder.objects.raw(
                        '''SELECT httc_order.id, httc_order.price, httc_order.action_type, httc_order.quantity,
                           SUM(markedskraft_trade.qty) as positions_quantity
                           FROM httc_order left outer join markedskraft_trade on httc_order.id = markedskraft_trade.httc_order_id
                           WHERE httc_order.order_status in ('new', 'pending', 'confirmed')
                           and httc_order.mk_contract_id = 1000
                           group by httc_order.id''' ))

ce(
    '''SELECT httc_order.id, httc_order.price, httc_order.action_type, httc_order.quantity,
       SUM(markedskraft_trade.qty) as positions_quantity
       FROM httc_order left outer join markedskraft_trade on httc_order.id = markedskraft_trade.httc_order_id
       WHERE httc_order.order_status in ('new', 'pending', 'confirmed')
       and httc_order.mk_contract_id = 1000
       group by httc_order.id''')


# 4st query
ce(
    '''SELECT `httc_order`.`id`, COUNT(`httc_order`.`id`) AS `count`
       FROM `httc_order`
       LEFT OUTER JOIN `markedskraft_trade` ON ( `httc_order`.`id` = `markedskraft_trade`.`httc_order_id_id` )
       WHERE (`httc_order`.`mk_contract_id` = 1000
       AND `httc_order`.`order_status` IN ('new', 'pending', 'confirmed')
       AND `markedskraft_trade`.`id` IS NULL)
       GROUP BY `httc_order`.`id`''')

t(HttcOrder.objects.filter(trade__isnull=True,
                           order_status__in=['new', 'pending', 'confirmed'],
                           mk_contract_id=1000).values('id').annotate(
    count=Count('id')).order_by('-price'))

t(HttcOrder.objects.raw(
                        '''SELECT `httc_order`.`id`, COUNT(`httc_order`.`id`) AS `count`
                           FROM `httc_order`
                           LEFT OUTER JOIN `markedskraft_trade` ON ( `httc_order`.`id` = `markedskraft_trade`.`httc_order_id_id` )
                           WHERE (`httc_order`.`mk_contract_id` = 1000
                           AND `httc_order`.`order_status` IN ('new', 'pending', 'confirmed')
                           AND `markedskraft_trade`.`id` IS NULL)
                           GROUP BY `httc_order`.`id`'''))
