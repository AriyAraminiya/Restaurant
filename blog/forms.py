from django import forms


class CommentForm(forms.Form):
    name = forms.CharField( max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    comment = forms.CharField(widget = forms.Textarea , required=True)


