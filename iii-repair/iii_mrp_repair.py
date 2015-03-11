from openerp.osv import fields, osv

class mrp_repair(osv.osv):

     _inherit = 'mrp.repair'
     _columns = {
                 'technician':fields.many2one('res.users','Technician')
                 }
     _defaults = {
                    'technician': lambda self, cr, uid, c: uid,
                 }