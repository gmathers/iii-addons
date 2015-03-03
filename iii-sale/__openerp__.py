{
    'name' : 'Custom iii Sales modifications',
    'version' : '1.0.0',
    'author' : 'Garth Mathers',
    'category' : 'Sales',
    'website' : '',
    'description': """
        Add default filter to Phonecalls action to only show current user's call
    """,
    'depends' : ['base', 'sale_crm'],
    'data':[
        'views.xml',
        ],
    'installable': True
}
