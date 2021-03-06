from django import forms
from .fields import RangeSliderField
from .models import Comment


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(
                                attrs={"class": "form-control",
                                       "placeholder": "Your Name"}))
    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Leave a comment!"}))
    # mc added per AS code
    slider_val = RangeSliderField(label=True, minimum=1, maximum=10)
