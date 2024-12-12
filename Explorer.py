# AutoExplorer Rise of Kingdoms PixelBot
import keyboard
import pywintypes
import pygetwindow as gw
from Clicks import *

def main():
    print('Iniciando . . .')
    while keyboard.is_pressed("Esc") != True:

        try:
            # Ventana del launcher siempre activa
            window_name = "Rise of Kingdoms"

            # Obtén la ventana por su nombre
            window = gw.getWindowsWithTitle(window_name)

            # Verifica si se encontró una ventana con ese nombre
            if len(window) > 0:
                # Si se encontró, verifica si la ventana está inactiva
                if not window[0].isActive:
                    # Activa la ventana
                    window[0].activate()
                else:
                    pass
            else:
                pass

            # Si crashea el juego, da clic en CONFIRMAR
            if pyautogui.locateOnScreen('./screenshots/Confirmar.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Confirmar.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso
                time.sleep(1)

                # Regresa a la aldea
                if pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.7) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.7)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

            # Damos click en el Edificio de investigación
            if pyautogui.locateOnScreen('./screenshots/ExplorerBuilding.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/ExplorerBuilding.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Click on Building')

            if pyautogui.locateOnScreen('./screenshots/ExplorerBuilding2.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas en pixeles del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/ExplorerBuilding2.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2

                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

                # Agrega un retraso antes de buscar otra vez la misma imagen
                time.sleep(1)
                print('Click on Building')

            if pyautogui.locateOnScreen('./screenshots/ExplorerBuilding3.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/ExplorerBuilding3.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2

                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

                # Agrega un retraso antes de buscar otra vez la misma imagen
                time.sleep(1)
                print('Click on Building')

            # Después, Detecta el botón de explorar en las opciones del edificio
            if pyautogui.locateOnScreen('./screenshots/Explore.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Explore.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Building Explore')

            # Posteriormente detecta si uno de los exploradores está disponible (Busca 2 veces el mismo botón)
            if pyautogui.locateOnScreen('./screenshots/Available.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Available.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Explore')
            
            # Envía al explorador
            if pyautogui.locateOnScreen('./screenshots/Enviar.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Enviar.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Explorer Sent')
            
            # Vuelve a tu aldea y empieza de nuevo (Botón programado para volver: [Space])
            if pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.6) != None \
                and pyautogui.locateOnScreen('./screenshots/Enviar.jpg', confidence = 0.6) == None \
                and pyautogui.locateOnScreen('./screenshots/Available.jpg', confidence = 0.6) == None:
                
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Back')

        except TypeError or OSError:
            time.sleep(0.01)

if __name__ == "__main__":
    main()