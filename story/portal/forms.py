from django import forms
from portal.models import Book, BookCategory

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        #my form dont want contain the following fields
        exclude = ['created_date','last_update','active']


