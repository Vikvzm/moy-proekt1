from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ['name', 'email', 'text_comments']

"""поисковая система"""
class SearchForm(forms.Form):
    query = forms.CharField()
