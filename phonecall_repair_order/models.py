from openerp import api, models, fields, SUPERUSER_ID


class crm_phonecall(models.Model):
    _inherit = "crm.phonecall"

    repair_id = fields.Many2one('mrp.repair', 'Repair Order')


class mrp_repair(models.Model):
    _inherit = 'mrp.repair'

    @api.one
    def _get_phonecall_count(self):
        self.phonecall_count = self.env['crm.phonecall'].search_count([('repair_id', '=', self.id)])

    phonecall_count = fields.Integer('Phonecalls Count', compute='_get_phonecall_count')

    def name_get(self, cr, uid, ids, context=None):
        #if not (context or {}).get('mrp_repair_extended_name'):
        #    return super(mrp_repair, self).name_get(cr, uid, ids, context=context)

        res = []
        for r in self.browse(cr, uid, ids, context=context):
            rman = r.name
            rmap = r.partner_id.display_name
            if rmap:
                name = rman + ' / ' + rmap
            else:
                name = rman
            # name = '%s [%s]' % (r.name, r.partner_id.display_name)
            res.append((r.id, name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            # Be sure name_search is symmetric to name_get
            ids = []
            name_splited = name.split('/')
            if len(name_splited) > 1:
                rman = name_splited[0]
                rmap = name_splited[1]
                ids += self.search(cr, uid, [('name', operator, rman),('partner_id.display_name', operator, rmap)] + args, limit=limit, context=context)
            else:
                ids += self.search(cr, uid, ['|',('name', operator, name),('partner_id.display_name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)


