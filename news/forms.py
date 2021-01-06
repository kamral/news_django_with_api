from django import forms

from .models import Category,News


class NewsForm(forms.ModelForm):

    class Meta:
        model=News
        fields=['title','content','category','is_published','photo']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows':5
            }),
            'is_published': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }
