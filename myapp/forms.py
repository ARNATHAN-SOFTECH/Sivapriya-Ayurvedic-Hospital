from django import forms
from .models import Bill, Patient


class BillForm(forms.ModelForm):

    class Meta:

        model = Bill

        fields = [
            "payment_method",
            "paid_amount",
            "notes",
        ]

        widgets = {

            "payment_method": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "paid_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "paidAmount",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "Enter paid amount",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional billing notes",
                }
            ),
        }