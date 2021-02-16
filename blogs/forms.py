from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['topic', 'details']
        labels = {'topic': '', 'details': ''}
        widgets = {'details': forms.Textarea(attrs={'cols': 120, 'rows': 50}), 'topic': forms.Textarea(attrs={'cols': 40, 'rows': 2})}
