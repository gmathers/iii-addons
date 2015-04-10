from openerp.osv import fields, osv

class crm_lead(osv.osv):
    _name = 'crm.lead'
    _inherit = 'crm.lead'

    _columns = {
        'stage_id': fields.many2one('crm.case.stage', 'Stage', track_visibility='onchange', select=True,
                        domain="['&', ('section_ids', '=', section_id), '|', ('type', '=', type), ('type', '=', 'both')]",
                        help='\'Marketing Qualified\' 3 of 5 MANTS criteria met.\n'
                             '\'Sales Qualified\' 5 of 5 MANTS criteria met.\n'
                             '\'Champion\' Our contact has started to champion this opp.\n'
                             '\'Evaluation\' They have started the evaluation process.\n'
                             '\'Proposal\' Our solution matches their goals and pricing was sent.\n'
                             '\'Negotiation/Review\' We are on the \"short list\" and are negotiating.\n'
                             '\'Won\' The deal has been closed, the order is in hand.\n'
                             '\'Lost\' The deal has been lost to competition or \"no decision\".\n'
                             '\'Inactive\' No response (phone/email) from contact in 60 days.'),
    }