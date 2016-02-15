from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields are what we want users to be able to input
        # timestamp and updated are both columns in our database, but we don't necessarily want users to be able to input when they were created or updated
        fields = [

            "title",
            "image",
            "content",

        ]
