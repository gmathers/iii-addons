{
    'name' : 'Custom iii CRM modifications',
    'version' : '1.0.0',
    'author' : 'Garth Mathers',
    'category' : 'CRM',
    'website' : '',
    'description': """
        Custom Filters and Groups on CRM Opportunities Kanban View
        Customize Field Order on CRM Opportunities Kanban View
    """,
    'depends' : ['base', 'sale_crm'],
    'data':[
        'views.xml',
        ],
    'installable': True
}
