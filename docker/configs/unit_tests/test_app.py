import unittest
from unittest.mock import patch
import json
from app import app, get_welcome_data

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.mysql.connector.connect')
    def test_index(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [("1", "Welcome to devops_app!")]

        # Mensaje descriptivo de inicio de la prueba
        print("Iniciando test_index: se verificará que la página de inicio se cargue correctamente...")

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenidos a devops_app!', response.data)

        # Mensaje descriptivo de fin de la prueba
        print("Test test_index completado. La página de inicio se cargó correctamente.")

    @patch('app.mysql.connector.connect')
    def test_welcome(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [("1", "Welcome to devops_app!")]

        # Mensaje descriptivo de inicio de la prueba
        print("Iniciando test_welcome: se verificará que los datos de bienvenida se obtengan correctamente...")

        response = self.app.get('/welcome')
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIn(["1", "Welcome to devops_app!"], response_data)

        # Mensaje descriptivo de fin de la prueba
        print("Test test_welcome completado. Los datos de bienvenida se obtuvieron correctamente.")

if __name__ == '__main__':
    unittest.main()
