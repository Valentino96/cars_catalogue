from django import forms

from cars_catalogue.cars.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Car
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

