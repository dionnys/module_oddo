{
    'name': 'Movie Manager',
    'version': '1.0',
    'summary': 'Gestión de películas desde API externa',
    'description': 'Módulo que permite gestionar películas,.',
    'author': 'dionnys',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/movie_views.xml',
        'data/config_parameters.xml',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
}
