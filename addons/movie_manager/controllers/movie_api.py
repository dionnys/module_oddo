from odoo import http
from odoo.http import request
import json

class MovieController(http.Controller):

    @http.route('/api/top_movies', auth='public', type='http', methods=['GET'], csrf=False)
    def get_top_movies(self, **kw):
        movies = request.env['movie.movie'].sudo().search(
            [],
            order='ranking desc',
            limit=10
        )
        result = [
            {
                'id': movie.id,
                'name': movie.name,
                'ranking': movie.ranking
            }
            for movie in movies
        ]
        return request.make_response(
            json.dumps(result, ensure_ascii=False),
            headers=[('Content-Type', 'application/json')]
        )
