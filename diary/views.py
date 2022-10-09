from django.shortcuts import render, redirect
from .models import DiaryEntry
from diary.forms import NewEntryForm
from django.views import View


# Create your views here.
def get_landing_page(request):
    return render(request, 'index.html')


def get_sign_up_page(request):
    return render(request, 'sign-up.html')


def create_entry(request):
    return render(request, 'create_new_entry.html')


class PostDetail(View):

    def get(self, request, *args, **kwargs):
        entry_form = NewEntryForm()
        return render(
            request,
            'create_new_entry.html',
            {
                'entry_form': entry_form,
            }
        )
