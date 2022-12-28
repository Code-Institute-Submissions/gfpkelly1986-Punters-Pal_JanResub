from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import DiaryEntry
from diary.forms import NewEntryForm
from django.views import generic, View
from django.contrib.auth.models import User


# Create your views here.
def get_landing_page(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/signup/')
def get_create_entry_page(request):
    return render(request, 'create_new_entry.html')


@login_required()
def delete_entry(request, entry_id):
    entries = DiaryEntry.objects.all()
    entry = get_object_or_404(entries, id=entry_id)
    if entry.created_by != request.user:
        return render(request, '404.html')
    else:
        entry.delete()
        return redirect('all-entries')


def error_404_view(request, exception):
    return render(request, '404.html')


@method_decorator(login_required, name='dispatch')
class ShowDiaryEntries(View):

    def get(self, request, *args, **kwargs):
        entries = DiaryEntry.objects.filter(created_by=request.user)
        paginate_by = 3
        return render(
            request,
            'diary_display.html',
            {
                'entries': entries,
            })


@method_decorator(login_required, name='dispatch')
class SearchResults(View):

    def post(self, request, *args, **kwargs):
        entries = DiaryEntry.objects.all()
        search_entry = request.POST['diary-search']
        entry = get_object_or_404(entries, horse_name=search_entry)

        return render(
            request,
            'search_results.html',
            {
                'search_entry': search_entry,
                'entry': entry
            }
        )


@method_decorator(login_required, name='dispatch')
class EditDiaryEntry(View):

    def get(self, request, entry_id, *args, **kwargs):
        entries = DiaryEntry.objects.all()
        entry = get_object_or_404(entries, id=entry_id)
        if entry.created_by != request.user:
            return render(request, '404.html')
        else:
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
            instance.created_by = User.objects.get(
                username=request.user.username)
            instance.save()

        return redirect('diary_display.html')
