from django import forms
from .models import Post, BlogComment


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment', ]



