
from datetime import datetime, timedelta
import time
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from openerp import workflow


class sale_order(osv.osv):

    _inherit = 'sale.order'

    _columns = {
#        'sale_etc': fields.text('Default Terms and Conditions'),
    }

    def print_label_1(self, cr, uid, ids, context=None):

        return self.pool['report'].get_action(cr, uid, ids, 'label_4devnet.report_label', context=context)

    def print_label_2(self, cr, uid, ids, context=None):

        return self.pool['report'].get_action(cr, uid, ids, 'label_4devnet.report_label_2', context=context)
	

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    def print_label_1(self, cr, uid, ids, context=None):

        return self.pool['report'].get_action(cr, uid, ids, 'label_4devnet.report_partner_label', context=context)