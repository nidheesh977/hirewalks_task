from django.forms import ModelForm
from .models import Address, CustomUser

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            "title",
            "fullName",
            "addressLine1",
            "addressLine2",
            "city",
            "state",
            "pincode",
            "country",
            "mobile"
        ]


class SignupForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "is_seller"]