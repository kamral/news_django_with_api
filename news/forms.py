from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100,label='Название',
                            widget=forms.TextInput(
                                attrs={'class':'form-control'}
                            ))
    content = forms.CharField(required=False,label='Текст:',
                              widget=forms.Textarea(
                                  attrs={'rows':5,
                                      'class': 'form-control'}
                              )
                              )
    is_published = forms.BooleanField(label='Опубликованно',
                                      initial=True,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control'}
                                      )
                                      )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категория',
                                      empty_label='Выберите Категорию',
                                      widget=forms.Select(
                                          attrs={'class': 'form-control'}
                                      )
                                      )

