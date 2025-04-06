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
    'assets': {
        'web.assets_backend': [
        'movie_manager/static/src/js/movie_autorefresh.js',
        ],
    },
    'installable': True,
    'application': True,
}
