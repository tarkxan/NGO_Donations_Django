from decimal import Decimal

from django.core.validators import MinValueValidator
from django.forms import forms, DecimalField, BooleanField, CharField
from donation.models import DonationType, DonationUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.db import transaction


class DonationCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DonationCreateForm, self).__init__(*args, **kwargs)
        objs = DonationType.objects.filter(is_active=True)
        for obj, i in zip(objs, range(len(objs))):
            self.fields['amount_{}'.format(obj.pk)] = DecimalField(
                max_digits=12, decimal_places=2,
                validators=[MinValueValidator(Decimal(0.01))],
                required=False
            )
            self.fields['amount_{}'.format(obj.pk)].label = obj.name
            self.fields['recurring_{}'.format(obj.pk)] = BooleanField(required=False)
            self.fields['recurring_{}'.format(obj.pk)].label = 'recurring' if obj.monthly_billing else ''
        self.fields['user_id'] = CharField(max_length=100)


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = DonationUser

        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        return user
