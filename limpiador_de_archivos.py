import os
import sys
import ctypes
import shutil

def limpiar_carpeta(ruta):
    """Elimina todo el contenido dentro de una carpeta sin borrar la carpeta principal"""
    if os.path.exists(ruta):
        for archivo in os.listdir(ruta):
            archivo_path = os.path.join(ruta, archivo)
            try:
                if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                    os.unlink(archivo_path)  # Eliminar archivos y enlaces simbólicos
                elif os.path.isdir(archivo_path):
                    shutil.rmtree(archivo_path)  # Eliminar carpetas y su contenido
            except Exception as e:
                print(f"No se pudo eliminar {archivo_path}: {e}")
    else:
        print("La carpeta no existe.")

def solicitar_admin():
    """Reinicia el script con privilegios de administrador si no los tiene"""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Solicitando permisos de administrador...")
        script = sys.executable
        params = " ".join([f'"{arg}"' for arg in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)
        


# Definir la ruta de la carpeta
if __name__ == "__main__":
    rutas_carpetas = [r"C:\Windows\Prefetch", r"C:\Windows\Temp", r"C:\Users\USER\AppData\Local\Temp"]
    try:
        # solicitar_admin()
        for i in rutas_carpetas:
            limpiar_carpeta(i)
            print(f"Se limpio correctamente la ruta: {i}")
            print(f"{rutas_carpetas.index(i)+1} / {len(rutas_carpetas)} tareas completadas")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        sys.exit()