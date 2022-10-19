from django.test import TestCase
from diary.forms import NewEntryForm
from diary.models import DiaryEntry


# Create your tests here.
class TestItemForm(TestCase):

    def test_created_by_field_is_not_required_for_valid_form(self):
        form = NewEntryForm(
            {'race_title': 'test',
                'race_type': 'test',
                'horse_name': 'test',
                'grade': 3,
                'distance': 'test',
                'going': 'test',
                'trainer': 'test',
                'jockey': 'test',
                'num_of_runners': 9,
                'result_of_entry': 1,
                'result_1': 'test',
                'result_2': 'test',
                'result_3': 'test',
                'note_detail': 'test'})
        self.assertTrue(form.is_valid())

    def test_race_type_is_required(self):
        form = NewEntryForm(
            {'race_title': '',
                'race_type': 'test',
                'horse_name': 'test',
                'grade': 3,
                'distance': 'test',
                'going': 'test',
                'trainer': 'test',
                'jockey': 'test',
                'num_of_runners': 9,
                'result_of_entry': 1,
                'result_1': 'test',
                'result_2': 'test',
                'result_3': 'test',
                'note_detail': 'test'})
        self.assertFalse(form.is_valid())

    def test_form_model_uses_DiaryEntry_model(self):
        form = NewEntryForm()
        self.assertEqual(form.Meta.model, DiaryEntry)
