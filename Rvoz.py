import speech_recognition as sr
import subprocess
import pyautogui
import webbrowser
import os

recognizer = sr.Recognizer()
proceso = None
saludo = """Hola Gente, como vamos?
"""
presentar= """
Mi Nombre es Rvoz soy un programa hecho en python capaz de entender la voz de las personas y procesar lo que me dicen segun los comandos que he aprendido
"""
despedir= """
Adios gente :)
"""

#Funciones
def cerrar_calculadora():
    try:
        os.system("taskkill /f /im calc.exe")
        print("Calculadora cerrada.")
    except Exception as e:
        print(f"Error al cerrar la Calculadora: {e}")


def cerrar_notepad():
    try:
        os.system("taskkill /f /im notepad.exe")
        print("Bloc de notas cerrado.")
    except Exception as e:
        print(f"Error al cerrar el Bloc de notas: {e}")
def abrir_navegador():
    webbrowser.open("https://www.google.com")

def abrir_youtube():
    webbrowser.open("https://www.youtube.com")

def abrir_calculadora():
    subprocess.Popen(["calc.exe"])

def abrir_notepad():
    proceso = subprocess.Popen(["notepad.exe"])

   



def buscar_en_youtube(query):
    base_url = "https://www.youtube.com/results?search_query="
    query_url = base_url + "+".join(query.split())
    webbrowser.open(query_url)


def ejecutar_comando(comando):
    global proceso
    comando = comando.lower()  # Convertir a minúsculas para hacerlo case-insensitive

    if "abrir notepad" in comando:
       abrir_notepad()
    elif "saludar gente" in comando:
        pyautogui.write(saludo)

    elif "preséntate" in comando:
        pyautogui.write(presentar)

    elif "despídete" in comando:
        pyautogui.write(despedir)

    elif "cerrar notepad" in comando:
       cerrar_notepad()
            
    elif "abrir calculadora" in comando:
        abrir_calculadora()

    elif "cerrar calculadora" in comando:
       
       cerrar_calculadora()
        
    elif "abrir navegador" in comando:
        abrir_navegador()

    elif "abrir youtube" in comando:
        abrir_youtube()

    elif "buscar en youtube" in comando:
        # Extraer la consulta de búsqueda
        inicio_busqueda = comando.find("buscar en youtube") + len("buscar en youtube")
        query = comando[inicio_busqueda:].strip()
        buscar_en_youtube(query)

    elif "apagar" in comando:
        print("¡Apagando el programa!")
        exit()
    else:
        print("Comando no reconocido.")

    



def escuchar_comandos():
    with sr.Microphone() as source:
        print("como puedo ayudarte?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"comando reconocido:{comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("no se pudo entender el comando")

    except sr.UnknownValueError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comandos()