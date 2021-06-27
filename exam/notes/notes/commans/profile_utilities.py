from notes.profiles.models import Profile
from notes.users_notes.models import Note

def get_profile():
    profile = Profile.objects.first()

    if profile:
        notes = Note.objects.all()

    return profile
