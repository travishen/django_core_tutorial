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
        exclude = []

    def save(self, commit=True, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.save()
