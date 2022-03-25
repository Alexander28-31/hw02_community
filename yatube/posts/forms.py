
from django import forms

from .models import Post


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        label = {
            'text': ('Текст поста'),
            'group': ('Группа поста')
        }
