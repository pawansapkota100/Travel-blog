
from django.forms import ModelForm
from .models import Blog,ClientMessage,Contact

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