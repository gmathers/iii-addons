# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'MRP-Custom Module',
    'version': '1.1',
    'category': 'mrp_repair',
  #  'sequence': 19,
  #  'summary': 'Purchase Orders, Receptions, Supplier Invoices',
    'description': """    
    For customized Partner & product screen with button link to Repair Order.
    """,
    'author': '4devnet.com',
    'website': 'http://www.4devnet.com',
 #   'images' : ['images/purchase_order.jpeg', 'images/purchase_analysis.jpeg', 'images/request_for_quotation.jpeg'],
    'depends': ['product','base','mrp_repair'],
    'data': [
        #'abc_report.xml',
        'mrp_custom.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
