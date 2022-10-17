from django.test import TestCase
from diary.models import DiaryEntry
from django.contrib.auth.models import User


# Create your tests here.
class TestDiaryViews(TestCase):
    def test_get_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_sign_up_page(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_get_login_page(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_get_logout_page_redirect(self):
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 302)

    def test_get_diary_display_page(self):
        response = self.client.get('/diary_display.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary_display.html')

    def test_create_new_entry_page(self):
        response = self.client.get('/create_new_entry')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_new_entry.html')

    #To-Do: Create a user instance in the test so created_by field works in test.
    # def test_edit_entry_page(self):
    #     user = self.client.get()
    #     entry = DiaryEntry.objects.create(
    #         race_title='test',
    #         race_type='test',
    #         created_by=User,
    #         horse_name='test',
    #         grade=4,
    #         distance='test',
    #         going='test',
    #         trainer='test',
    #         )
    #     response = self.client.get(f'/edit_entry/{entry.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'edit_entry.html')
