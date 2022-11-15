from django.shortcuts import render, get_object_or_404, redirect
from .models import DiaryEntry
from diary.forms import NewEntryForm
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
def get_landing_page(request):
    return render(request, 'index.html')


def get_create_entry_page(request):
    return render(request, 'create_new_entry.html')


def delete_entry(request, entry_id):
    entries = DiaryEntry.objects.all()
    entry = get_object_or_404(entries, id=entry_id)
    entry.delete()
    return redirect('all-entries')


class ShowDiaryEntries(View):

    def get(self, request, *args, **kwargs):
        entries = DiaryEntry.objects.filter(created_by=request.user)
        return render(
            request,
            'diary_display.html',
            {
                'entries': entries,
            })


class SearchResults(View):

    def post(self, request, *args, **kwargs):
        return render(
            request,
            'search_results.html')


class EditDiaryEntry(View):

    def get(self, request, entry_id, *args, **kwargs):
        entries = DiaryEntry.objects.all()
        entry = get_object_or_404(entries, id=entry_id)
        edit_form = NewEntryForm(instance=entry)
        return render(
            request,
            'edit_entry.html',
            {
                'edit_form': edit_form
            }
        )

    def post(self, request, entry_id, *args, **kwargs):
        entries = DiaryEntry.objects.all()
        entry = get_object_or_404(entries, id=entry_id)
        update_form = NewEntryForm(data=request.POST, instance=entry)
        if update_form.is_valid():
            update_form.save()

        return redirect('all-entries')


class NoteDetail(View):

    def get(self, request, *args, **kwargs):
        entry_form = NewEntryForm()
        return render(
            request,
            'create_new_entry.html',
            {
                'entry_form': entry_form,
            }
        )

    def post(self, request, *args, **kwargs):
        new_entry = NewEntryForm(data=request.POST)
        if new_entry.is_valid():
            instance = new_entry.save(commit=False)
            instance.created_by = User.objects.get(username=request.user.username)
            instance.save()

        return redirect('diary_display.html')
