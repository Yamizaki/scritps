# Limpieza de Archivos Temporales en Windows

Este script en Python se encarga de **eliminar el contenido de carpetas temporales** en un sistema Windows sin borrar las carpetas principales. También puede solicitar permisos de administrador si es necesario.

## 📌 Características
- **Elimina archivos y subcarpetas** de directorios específicos.
- **Solicita permisos de administrador** si no se ejecuta con privilegios elevados.
- **Evita errores y muestra progreso** en la limpieza.

## 📂 Carpetas que se limpian
El script está configurado para limpiar las siguientes carpetas:
- `C:\Windows\Prefetch`
- `C:\Windows\Temp`
- `C:\Users\USER\AppData\Local\Temp`

## 🚀 Instalación y Uso
### 1️⃣ Requisitos
- Python 3 instalado en tu sistema.
- Permisos de administrador para eliminar archivos protegidos del sistema.

### 2️⃣ Ejecución del Script
1. **Ejecutar como administrador**: Abre una terminal como administrador.
2. **Ejecutar el script**:
   ```sh
   python script.py
   ```

## 📜 Explicación del Código
### **1. Función `limpiar_carpeta(ruta)`**
Limpia todo el contenido de una carpeta específica:
- Si el archivo es normal o un enlace simbólico, lo elimina (`os.unlink()`).
- Si el archivo es una carpeta, la borra junto con su contenido (`shutil.rmtree()`).
- Si la carpeta no existe, muestra un mensaje de error.

### **2. Función `solicitar_admin()`**
Verifica si el script tiene permisos de administrador:
- Si **no** tiene permisos, reinicia el script con privilegios elevados usando `ctypes.windll.shell32.ShellExecuteW()`.
- Si **ya** tiene permisos, continúa la ejecución normalmente.

### **3. Bloque Principal (`if __name__ == "__main__":`)**
- Define las rutas de las carpetas a limpiar.
- Llama a `solicitar_admin()` (opcional, actualmente comentado).
- Ejecuta `limpiar_carpeta()` en cada carpeta de la lista.
- Muestra mensajes de progreso y maneja errores.

## ⚠️ Advertencia
- Este script elimina archivos **sin opción de recuperación**. Asegúrate de que no haya archivos importantes en las carpetas que se limpiarán.

## 📄 Licencia
Este código es de uso libre. Puedes modificarlo y adaptarlo según tus necesidades.

