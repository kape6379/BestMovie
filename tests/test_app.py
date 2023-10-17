import unittest
from src.app import app
from unittest.mock import patch
from database_support.db import MovieRating


class TestApp(unittest.TestCase):
    def setup(self):
        self.app = app.test_client()
        self.app.testing = True
        self.app_context().push()

    @patch('database_support.db.MovieRating.query.filter')
    def test_best_movies(self, mock_filter):
        fake_movie = MovieRating(title='FakeMovie', rating=99)
        additional_fake_movie = MovieRating(title="AdditionalFakeMovie", rating=97)
        mock_filter.return_value.all.return_value = [fake_movie, additional_fake_movie]

        response = self.app.get('/best_movies')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
