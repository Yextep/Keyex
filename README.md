# Registrador De Pulsaciones De Teclas

Este script es un keylogger, una herramienta que registra las pulsaciones de teclas en un sistema informático. Su principal propósito es registrar y almacenar la información de las teclas presionadas por un usuario en un archivo de registro. Esto se hace para diversos fines, como monitorear la actividad del usuario, diagnosticar problemas, o, en algunos casos, para propósitos maliciosos, como robar información confidencial. En este caso, el script registra las pulsaciones de teclas legibles y filtra combinaciones no deseadas, lo que puede ser útil en situaciones legítimas, como monitoreo de la actividad en una computadora. Sin embargo, es importante tener en cuenta que el uso de keyloggers debe cumplir con las leyes y regulaciones aplicables y respetar la privacidad de los usuarios.

<img align="center" height="480" width="1000" alt="GIF" src="https://github.com/Yextep/Keyex/assets/114537444/2f73d83f-7946-4244-b5a3-a671db7ffde4"/>

Las mejoras en el código incluyen la adición de un filtrado más estricto de las combinaciones de teclas no deseadas que comienzan con "Key." y la reestructuración del código en una clase para una mejor organización y mantenibilidad. Esto permite un mejor control sobre las pulsaciones de teclas registradas y garantiza que solo se almacenen las pulsaciones de teclas legibles, mejorando la calidad del registro de frases.

# Características principales

- 📌 Se importan los módulos necesarios: pynput.keyboard, datetime y signal para capturar señales.
  
- 📌 Se crea una clase Keylogger para encapsular la funcionalidad del keylogger y gestionar las pulsaciones de teclas.
  
- 📌 En la función is_modifying_key, se define una lista de teclas de modificación, como Ctrl, Alt, Shift y Cmd, y se comprueba si la tecla actual es una de ellas.
  
- 📌 En on_press, se capturan las pulsaciones de teclas. Se verifica si la tecla actual es una tecla de modificación y se descarta si lo es. Luego, se intenta obtener el carácter asociado a la tecla. Si es un carácter imprimible, se agrega a la lista current_keys. Si es un espacio, se agrega un espacio en blanco. Si es Enter, se guarda el registro en el archivo y se borra la lista current_keys. Si es Backspace, se elimina el último carácter de la lista. Se filtran todas las teclas que comienzan con "Key.".
  
- 📌 La función save_log guarda el registro actual en el archivo de registro con una marca de tiempo.

- 📌 La función start inicia el keylogger y configura un manejador de señal para capturar Ctrl+C y detener el programa de manera ordenada.

- 📌 La función ctrl_c_handler se encarga de guardar el registro antes de salir del programa al presionar Ctrl+C.
  
# Instalación

Clonamos el repositorio
```bash
git clone https://github.com/Yextep/Keyex
```
Accedemos a la carpeta
```bash
cd Keyex
```
Instalamos requerimientos
```bash
pip install -r requeriments.txt
```
Ejecutamos el Script
```bash
python3 key.py
```
