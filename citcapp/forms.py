from django import forms
from citcapp.models import CityModel,CustomerModel

class CityForm(forms.ModelForm):

    class Meta:
        model = CityModel
        fields = "__all__"


    def clean_pin_code(self):
        pin = self.cleaned_data["pin_code"]
        if pin in [500050,500045,500047,500049,500048,500046]:

            return pin
        else:
            raise forms.ValidationError("Invalid Pincode")

class CustomerForm(forms.ModelForm):
    cus_ID = forms.IntegerField(min_value=101)
    class Meta:
        model = CustomerModel
        fields = "__all__"

