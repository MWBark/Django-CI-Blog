from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

# Create your tests here.
class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about = About(title="About title", content="About content")
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaborate_form_submission(self):
        """Test for posting a collaboration form"""
        post_data = {
            'name': 'Testy McTest',
            'email': 'testmctest@fakemail.com',
            'message': 'Wanna collab?'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content
        )

