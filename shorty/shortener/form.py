from django import forms


from .models import URL


class URLForm(forms.ModelForm):
    full_url = forms.URLField(label="URL", help_text="Enter your to hash")
    class Meta:
        model = URL
        fields = ("full_url", )