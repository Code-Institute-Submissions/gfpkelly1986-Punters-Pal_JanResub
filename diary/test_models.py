from django.test import TestCase
from diary.models import DiaryEntry
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_created_by_instance(self):
        user = User.objects.create_user('gerkellytest')
        entry = DiaryEntry.objects.create(
            race_title='test',
            race_type='test',
            created_by=user,
            horse_name='test',
            grade=4,
            distance='test',
            num_of_runners=5,
            result_of_entry=1,
            going='test',
            trainer='test',
            )
        created_name = entry.created_by
        self.assertIsInstance(entry, DiaryEntry)
        self.assertEqual(created_name, user)

    def test_DiaryEntry_string_method_returns_race_title(self):
        user = User.objects.create_user('gerkellytest')
        entry = DiaryEntry.objects.create(
            race_title='return_title',
            race_type='test',
            created_by=user,
            horse_name='test',
            grade=4,
            distance='test',
            num_of_runners=5,
            result_of_entry=1,
            going='test',
            trainer='test',
            )
        self.assertEqual(str(entry), 'return_title')
