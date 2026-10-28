from django import forms
from .models import CarModel

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"
        labels = {
            "car" : "brand_name",
            "color" : "shades",
            "price" : "paise"
        }

        widgets = {
            "car" : forms.TextInput(
                attrs= {
                    "placeholder" : "enter the car name",
                    "class" : "car_class"
                }
            ),
            "price" : forms.NumberInput(
                attrs={
                    "placeholder" : "paise paise",
                    "class" : "car_class"
                }
            )
        }