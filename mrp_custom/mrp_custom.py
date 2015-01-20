import time
import pytz
import urllib
from openerp import SUPERUSER_ID
from datetime import datetime
from dateutil.relativedelta import relativedelta

from openerp.osv import fields, osv
from openerp import netsvc
from openerp import pooler
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.osv.orm import browse_record, browse_null
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP
from openerp.osv import fields,osv
 
class product_template(osv.Model):
    _inherit = 'product.template'
    
    def action_view_repair(self, cr, uid, ids, context=None):
        act_obj = self.pool.get('ir.actions.act_window')
        mod_obj = self.pool.get('ir.model.data')
        product_ids = []
        for template in self.browse(cr, uid, ids, context=context):
            product_ids += [x.id for x in template.product_variant_ids]
        result = mod_obj.xmlid_to_res_id(cr, uid, 'mrp_repair.action_repair_order_tree',raise_if_not_found=True)
        result = act_obj.read(cr, uid, [result], context=context)[0]
        result['domain'] = "[('product_id','in',[" + ','.join(map(str, product_ids)) + "]),('state', '!=', 'cancel')]"
        return result
    
    def _repair_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        for template in self.browse(cr, uid, ids, context=context):
            res[template.id] = sum([p.repair_count for p in template.product_variant_ids])
        return res
     
    _columns = {
                    'repair_count': fields.function(_repair_count, string='# REpair', type='integer'), 
                } 
    
class product_product(osv.Model):
    _inherit = 'product.product'
    
    def _repair_count(self, cr, uid, ids, field_name, arg, context=None):
        OrderRepair = self.pool['mrp.repair']
        return {
            product_id: OrderRepair.search_count(cr,uid, [('product_id', '=', product_id),('state', '!=', 'cancel')], context=context)
            for product_id in ids
        }   
    
    _columns = {
        'repair_count': fields.function(_repair_count, string='# REpair', type='integer'), 
            }
    
class res_partner(osv.osv):
    
    _inherit = 'res.partner'   
    
    def _repair_count(self, cr, uid, ids, field_name, arg, context=None):
        OrderRepair = self.pool['mrp.repair']
#         print 'OrderRepair............................'
#         print OrderRepair
        partner_ids = []
        for partner in self.browse(cr, uid, ids, context=context):
#             print 'partner............................'
#             print partner 
            partner_ids.append(partner.id)
#             print partner_ids
#             print partner_ids[0]
        cr.execute("select id from res_partner where parent_id=%s",(partner_ids[0],))
        res_child=cr.fetchall()        
        if res_child:
            for child in res_child:
#                 print 'child --------------------------------------'
#                 print child
#                 print child[0]
                partner_ids.append(child[0])
        return {
            partner_id: OrderRepair.search_count(cr,uid, [('partner_id', '=', res_child + partner_ids),('state', '!=', 'cancel')], context=context)
            for partner_id in ids
                }
        
    def action_view_repair(self, cr, uid, ids, context=None):
        act_obj = self.pool.get('ir.actions.act_window')
        mod_obj = self.pool.get('ir.model.data')
        partner_ids = []
#         print ids
        for partner in self.browse(cr, uid, ids, context=context):
#             print 'partner............................'
#             print partner 
            partner_ids.append(partner.id)
#             print partner_ids
#             print partner_ids[0]
        cr.execute("select id from res_partner where parent_id=%s",(partner_ids[0],))
        res_child=cr.fetchall()
        
        if res_child:
            for child in res_child:
#                 print 'child --------------------------------------'
#                 print child
#                 print child[0]
                partner_ids.append(child[0])
        result = mod_obj.xmlid_to_res_id(cr, uid, 'mrp_repair.action_repair_order_tree',raise_if_not_found=True)
#         print result        
#         print '1111111111_______________________'
        result = act_obj.read(cr, uid, [result], context=context)[0]
#         print result      
        result['domain'] = "[('partner_id','in',[" + ','.join(map(str, partner_ids)) + "]),('state', '!=', 'cancel')]"
#         print result['domain']      
        return result

    def action_view_repair2(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        res = mod_obj.get_object_reference(cr,uid,'mrp_repair','action_repair_order_tree')
        res_id = res and res[1] or False
        return{
                'name':_('Repair Order'),
                'view_type':'tree',
                'view_mode':'tree,form',
                #'view_id':[res_id],
                'res_model':'mrp.repair',
                'type':'ir.actions.act_window',
                'target':'current',
              #  'context':'{partner_id:active_id}',                
               }
        
    _columns = {
        'repair_count': fields.function(_repair_count, string='# of Repair Order', type='integer'),
        'repair_count2': fields.function(_repair_count, string='# of Repair Order', type='integer'),
        'repair_ids': fields.one2many('mrp.repair','partner_id','Repaired Order')
    }

class mrp_repair(osv.osv): 
       
     _inherit = 'mrp.repair'
     _columns = {
                 'technician':fields.many2one('res.users','Technician')                 
                 }
     _defaults = {        
                    'technician': lambda self, cr, uid, c: uid,
                 }
        
        
        