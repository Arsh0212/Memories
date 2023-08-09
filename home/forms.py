from django import forms


class Login_form(forms.Form):
    Email_Id = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form_input",
                "placeholder": "Email",
            }
        ),
    )
    Password = forms.IntegerField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form_input", "placeholder": "Password", "id": "password"}
        ),
    )


class Signup_form(forms.Form):
    Name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form_input", "placeholder": "Name"}),
    )
    Age = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={"class": "form_input", "placeholder": "Age"}),
    )
    Email_Id = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={"class": "form_input", "placeholder": "Email"}),
    )
    Password = forms.IntegerField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form_input", "placeholder": "Password", "id": "password"}
        ),
    )
