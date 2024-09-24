
from django.forms import ModelForm
from .models import Blog,ClientMessage,Contact,Comment

class BlogForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Blog

class ContactForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = ClientMessage
        read_only_fields = ('created_at',)

class ContactUsForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Contact

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'website', 'comment']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['website'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Website'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Comment'})
