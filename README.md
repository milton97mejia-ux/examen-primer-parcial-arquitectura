# Analizador de Representación de Datos

Aplicación web desarrollada en **Python 3.12** y **Django** para la asignatura de **Arquitectura de Computadoras**. Relaciona sistemas numéricos, codificación de caracteres en memoria y ejecución de contenedores.

---

## 🚀 Instrucciones de Construcción y Ejecución

### Opción 1: Ejecución Local con Django
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

   ---

## 🧠 Consideraciones Teóricas y de Arquitectura

### 1. Recursos de la Arquitectura de Von Neumann en la Aplicación
La aplicación interactúa directamente con los principios fundamentales del modelo de Von Neumann:
* **Unidad aritmético-lógica (ALU) y Registros:** Se ven reflejados en las rutinas de conversión numérica (binario, octal, decimal y hexadecimal) y en el cálculo matemático de bits significativos y bytes necesarios.
* **Memoria Principal:** Se evidencia en el manejo y almacenamiento temporal de los datos ingresados por el usuario y en cómo la codificación de caracteres (como UTF-8 y la letra "ñ") mapea los puntos de código Unicode directamente a bytes en memoria.

### 2. ¿Por qué el contenedor comparte el kernel del host a diferencia de una máquina virtual?
A diferencia de una máquina virtual tradicional —la cual emula un sistema operativo completo con su propio kernel virtualizado sobre un hipervisor (lo que demanda una gran cantidad de recursos de hardware)—, **Docker utiliza la contenerización a nivel de sistema operativo**. Esto significa que el contenedor aísla los procesos, librerías y dependencias (como Python 3.12 y Django) utilizando directamente el **kernel del sistema operativo anfitrión (host)**. Como resultado, el contenedor es sumamente ligero, arranca en segundos y opera con restricciones estrictas de rendimiento (como los límites configurados de 256 MB de RAM y 1 CPU) sin la sobrecarga de virtualization por hardware completo.

---

## 🧪 Pruebas Automatizadas
Para ejecutar la suite de pruebas unitarias y verificar el funcionamiento lógico del sistema:
```bash
python manage.py test analizador