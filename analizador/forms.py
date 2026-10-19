from django import forms


class FormularioConversion(forms.Form):
    BASES_CHOICES = [
        (2, "Binario (Base 2)"),
        (8, "Octal (Base 8)"),
        (10, "Decimal (Base 10)"),
        (16, "Hexadecimal (Base 16)"),
    ]

    valor = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ej. 255, 1111, A0...",
            }
        ),
        label="Número a convertir",
    )
    base_origen = forms.ChoiceField(
        choices=BASES_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Base de Origen",
    )


class FormularioTexto(forms.Form):
    texto = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escribe un texto (máx. 20 caracteres, ej. Año)...",
            }
        ),
        label="Texto para análisis UTF-8",
    )