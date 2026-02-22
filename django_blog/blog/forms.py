from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a comment...'}),
        max_length=2000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        data = self.cleaned_data.get('content', '').strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        return data
