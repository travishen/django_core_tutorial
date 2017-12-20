from django import forms
import re
from .models import PostModel

class SearchForm(forms.Form):
    q = forms.CharField()


FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class TestForm(forms.Form):
    user_name = forms.CharField()
    is_root = forms.BooleanField()
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    USER_RE = re.compile(r"""\D +  # the none integral part
                             \.    # the decimal point
                             \w *  # some digits""", re.X)

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user_name'].initial = user.username

    def clean_user_name(self, *args, **kwargs):
        user_name = self.cleaned_data['user_name']
        if not TestForm.USER_RE.match(user_name):
            raise forms.ValidationError('User name format required [a-zA-Z].[a-zA-Z0-9]')
        return user_name


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel

        """Creating a ModelForm with either the 
        'fields' attribute or the 'exclude' 
        attribute is prohibited
        """
        fields = ['active', 'title', 'slug', 'content']
        # exclude = []
        labels = {
            'active': 'Active!',
            'slug': 'Slug!'
        }
        help_text = {
            'active': 'This is title label',
            'slug': 'This is slug label'
        }
        error_messages = {
            'title': {
                'max_length': 'This title is too long'
            }
        }

    def clean(self):
        print('validate title..')
        cleaned_data = super(PostModelForm, self).clean()
        title = cleaned_data.get('title')
        if 'test' not in title:
            raise forms.ValidationError("You have forgotten about test in title!")

        return cleaned_data

    def save(self, commit=True, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.save()

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)

        self.fields['title'].error_messages = {
            'max_length': 'This title is too long'
        }

        for field in self.fields.values():
            field.error_messages = {
                'max_length': '%s is too long' % field.label
            }



