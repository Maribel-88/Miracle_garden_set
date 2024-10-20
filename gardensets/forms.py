from django import forms
from .widgets import CustomClearableFileInput
from .models import Gardenset, Category


class GardenForm(forms.ModelForm):

    class Meta:
        model = Gardenset
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        basic_names = [(c.id, c.get_basic_name()) for c in categories]

        self.fields['category'].choices = basic_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'