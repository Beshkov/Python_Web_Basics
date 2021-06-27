from django import forms

from notes.users_notes.models import Note


class NotesForms(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class CreateNote(NotesForms):
    pass

class EditNote(NotesForms):
    pass

class DeleteNote(NotesForms):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
