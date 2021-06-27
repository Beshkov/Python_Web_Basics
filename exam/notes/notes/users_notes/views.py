from django.shortcuts import render, redirect

# Create your views here.
from notes.commans.profile_utilities import get_profile
from notes.users_notes.forms import CreateNote, EditNote, DeleteNote
from notes.users_notes.models import Note


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)

def add_note(request):
    if request.method == 'POST':
        form = CreateNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNote()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNote(instance=note)

    context = {
        'form': form,
    }

    return render(request, 'note-edit.html', context)

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        form = DeleteNote(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)