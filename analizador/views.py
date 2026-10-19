from django.shortcuts import render
from .forms import FormularioConversion, FormularioTexto
from .utils import convertir_numero, analizar_texto_utf8


def index(views_request):
    resultado_conversion = None
    error_conversion = None

    resultado_texto = None
    error_texto = None

    form_conv = FormularioConversion(views_request.POST or None, prefix="conv")
    form_txt = FormularioTexto(views_request.POST or None, prefix="txt")

    if views_request.method == "POST":
        # Identificar cuál formulario se envió
        if "btn_convertir" in views_request.POST:
            if form_conv.is_valid():
                valor = form_conv.cleaned_data["valor"]
                base_origen = int(form_conv.cleaned_data["base_origen"])
                try:
                    resultado_conversion = convertir_numero(valor, base_origen)
                except ValueError as e:
                    error_conversion = str(e)
            else:
                error_conversion = (
                    "Por favor, revise los datos ingresados en la conversión."
                )

        elif "btn_analizar" in views_request.POST:
            if form_txt.is_valid():
                texto = form_txt.cleaned_data["texto"]
                try:
                    resultado_texto = analizar_texto_utf8(texto)
                except ValueError as e:
                    error_texto = str(e)
            else:
                error_texto = "El texto excede el límite de 20 caracteres o es inválido."

    contexto = {
        "form_conv": form_conv,
        "resultado_conversion": resultado_conversion,
        "error_conversion": error_conversion,
        "form_txt": form_txt,
        "resultado_texto": resultado_texto,
        "error_texto": error_texto,
    }
    return render(views_request, "analizador/index.html", contexto)