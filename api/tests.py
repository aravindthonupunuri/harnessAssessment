from django.test import TestCase, Client
import hashlib
from datetime import date
from unittest import mock
from rest_framework.response import Response

# Assuming the necessary imports and setup for testing

class AddUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.mock_request_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
        }
    
    @mock.patch('api.userViews.make_request')
    def test_addUser_validData(self, mock_make_request):
        mock_make_request.side_effect = [
            {'deliverability': 'DELIVERABLE'},  # Mock email validation response
            {'city': 'Test City'},  # Mock location response
            [{'username': 'testuser'}]  # Mock holiday response
        ]
        
        expected_hashed_password = hashlib.sha256(b'password123').hexdigest()
        today = date.today()
        str_today = today.strftime("%Y-%m-%d")
        date_parts = str_today.split("-")
        
        expected_user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': expected_hashed_password,
            'city': 'Test City',
            'isHoliday': True
        }
        
        response = self.client.post('/addUser/', data=self.mock_request_data)
        
        self.assertEqual(response.status_code, 200)

    

    

