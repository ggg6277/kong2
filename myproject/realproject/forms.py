from django import forms
import datetime
from .models import Test, Image, Product, Comment, Post, Category

class RstForm(forms.ModelForm):
    subject=forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    summary= forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Leave a comment!"
            }
        )
    )
    upload_date=forms.DateField(initial=datetime.date.today)
    image=forms.ImageField()

    METHOD=(
        ('C','cash'),
        ('B', 'card'),
        ('P', 'point'),
    )
    acount=forms.CharField(label="What is your bill?", widget=forms.Select(choices=METHOD))

    class Meta:
        model=Test
        fields=('subject', 'image', 'summary', 'upload_date', 'acount')

class PrdctFrom(forms.ModelForm):
    code = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Product code"
        })
    )
    product = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Product name"
        })
    )
    price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder": "Price"
        })
    )
    exp_date = forms.DateField(initial=datetime.date.today)

    class Meta:
        model= Product
        fields=('code', 'product', 'price', 'exp_date')


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('title', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('author', 'body')

class BlogwriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'categories')

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

