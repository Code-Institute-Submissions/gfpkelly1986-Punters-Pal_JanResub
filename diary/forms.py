from diary.models import DiaryEntry
from django.forms import ModelForm


class NewEntryForm(ModelForm):
    class Meta:
        model = DiaryEntry
        fields = [
            'race_title',
            'race_type',
            'horse_name',
            'grade',
            'distance',
            'going',
            'trainer',
            'jockey',
            'num_of_runners',
            'result_of_entry',
            'result_1',
            'result_2',
            'result_3',
            'note_detail',
            ]
