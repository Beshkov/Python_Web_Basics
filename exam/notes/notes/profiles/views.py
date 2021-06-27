from django.shortcuts import render, redirect

# Create your views here.
from notes.commans.profile_utilities import get_profile
from notes.profiles.forms import ProfileForm
from notes.profiles.models import Profile
from notes.users_notes.models import Note


def profile_page(request):
    profile = get_profile()
    total_notes = len(Note.objects.all())

    context = {
        'profile': profile,
        'total_notes': total_notes,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method != 'POST':
        profile.delete()
        Note.objects.all().delete()
        return render(request, 'home-no-profile.html')


