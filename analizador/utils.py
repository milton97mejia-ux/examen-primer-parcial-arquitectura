def convertir_numero(valor, base_origen):
    """Convierte un número de una base origen (2, 8, 10, 16) a decimal,

    validando rangos y ajustando a bytes.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("El campo de entrada no puede estar vacío.")

    # Convertir a entero según la base de origen
    try:
        if base_origen == 2:
            num_decimal = int(str(valor), 2)
        elif base_origen == 8:
            num_decimal = int(str(valor), 8)
        elif base_origen == 10:
            num_decimal = int(str(valor), 10)
        elif base_origen == 16:
            num_decimal = int(str(valor), 16)
        else:
            raise ValueError("Base de origen no válida (debe ser 2, 8, 10 o 16).")
    except ValueError:
        raise ValueError(
            f"El valor '{valor}' no corresponde a un dígito válido para la base {base_origen}."
        )

    # Validar rango entre 0 y 65535
    if not (0 <= num_decimal <= 65535):
        raise ValueError(
            "El valor convertido está fuera del rango permitido (0 a 65535)."
        )

    # Representaciones en diferentes bases
    dec_str = str(num_decimal)
    oct_str = oct(num_decimal)[2:]
    hex_str = hex(num_decimal)[2:].upper()

    # Cálculo de bits significativos y ajuste a bytes
    if num_decimal == 0:
        bits_significativos = 1
    else:
        bits_significativos = num_decimal.bit_length()

    # Ajustar al siguiente límite de byte (8, 16, 24, etc.)
    total_bits = ((bits_significativos + 7) // 8) * 8
    if total_bits < 8:
        total_bits = 8

    bytes_necesarios = total_bits // 8
    bin_str = bin(num_decimal)[2:].zfill(total_bits)

    return {
        "decimal": dec_str,
        "binario": bin_str,
        "octal": oct_str,
        "hexadecimal": hex_str,
        "bits_significativos": bits_significativos,
        "bytes_necesarios": bytes_necesarios,
        "total_bits": total_bits,
    }


def analizar_texto_utf8(texto):
    """Analiza un texto de hasta 20 caracteres mostrando carácter,

    código decimal, punto de código U+, hexadecimal y bytes UTF-8.
    """
    if not texto or len(texto.strip()) == 0:
        raise ValueError("El texto no puede estar vacío.")
    if len(texto) > 20:
        raise ValueError("El texto excede el límite máximo de 20 caracteres.")

    resultados = []
    for c in texto:
        codigo_decimal = ord(c)
        punto_codigo = f"U+{codigo_decimal:04X}"
        hex_val = f"0x{codigo_decimal:02X}"

        # Obtener bytes en UTF-8
        bytes_utf8 = " ".join([f"0x{b:02X}" for b in c.encode("utf-8")])

        resultados.append(
            {
                "caracter": c,
                "decimal": codigo_decimal,
                "punto_codigo": punto_codigo,
                "hexadecimal": hex_val,
                "bytes_utf8": bytes_utf8,
            }
        )
    return resultados