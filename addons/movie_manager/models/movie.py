from odoo import models, fields, api
import requests
import logging


_logger = logging.getLogger(__name__)

class Movie(models.Model):
    _name = 'movie.movie'
    _description = 'Película'

    name = fields.Char(string='Título de la película')
    ranking = fields.Float(string='Ranking')

    @api.model
    def fetch_movies_from_api(self):

        api_url = self.env['ir.config_parameter'].sudo().get_param('movie_manager.api_url')

        _logger.info("Valor de api_url: %s", api_url)

        api_key = self.env['ir.config_parameter'].sudo().get_param('movie_manager.api_key')

        _logger.info("Valor de api_key: %s", api_key)


        if not api_url or not api_key:
            _logger.error("Faltan parámetros de configuración: api_url o api_key")
            return
        try:
            response = requests.get(f"{api_url}?api_key={api_key}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                _logger.info("Respuesta del API: %s", data)

                title = data.get("movie_title")
                ranking = float(data.get("ranking_movie", 0))

                if title:
                    self.create({
                        'name': title,
                        'ranking': ranking,
                    })
            else:
                _logger.error("API Error %s: %s", response.status_code, response.text)
        except Exception as e:
            _logger.exception("Error al consultar el API de películas: %s", e)
