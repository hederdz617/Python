import os

def ocultar_archivos_windows(carpeta):
    for archivo in os.listdir(carpeta):
        ruta_archivo= os.path.join(carpeta,archivo)
        if os.path.isfile(ruta_archivo):
            comando =f'attrib +h "{ruta_archivo}"'
            os.system(comando)
            print(f"Archivo ocultado: {ruta_archivo}")

carpeta="D:\\trabajos de progra\\ConsoleApp1\\CARPETA"
ocultar_archivos_windows(carpeta)
        