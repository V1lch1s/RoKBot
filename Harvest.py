import keyboard
import pywintypes
import pygetwindow as gw
from Clicks import *

def main():
    n = 0 # Regalos aceptados
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
                # Obtiene las coordenadas del centro de la imagen detectada
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
            if pyautogui.locateOnScreen('./screenshots/Explore.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Explore.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
                print('Building Explore')

            # Click en la pestaña de "Aldeas"
            if pyautogui.locateOnScreen('./screenshots/Aldeas.jpg', confidence = 0.6) != None:
                
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Aldeas.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)

            # Detecta si está disponible el botón Ir (Busca 2 veces el mismo botón)
            if pyautogui.locateOnScreen('./screenshots/Ir.jpg', confidence = 0.6) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Ir.jpg', confidence = 0.6)
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Mueve el mouse al centro de la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso antes de buscar la imagen nuevamente
                time.sleep(1)
            
            # Detecta la aldea tribal
            if pyautogui.locateOnScreen('./screenshots/Gift.jpg', confidence = 0.8) \
                or pyautogui.locateOnScreen('./screenshots/Gift2.jpg', confidence = 0.8):
                if pyautogui.locateOnScreen('./screenshots/Gift2.jpg', confidence = 0.8):
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Gift2.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2) + 50 # Debe hacer el click debajo de la imagen
                    
                    # Mueve el mouse debajo de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1.5)

                    # Acepta el regalo
                    leftClick(center_x, center_y)
                    n += 1

                else:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Gift.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2) + 50 # Debe hacer el click debajo de la imagen
                    
                    # Mueve el mouse debajo de la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)

                    # Agrega un retraso
                    time.sleep(1.5)

                    # Acepta el regalo
                    leftClick(center_x, center_y)
                    n += 1
                    
                    # Agrega un retraso antes de buscar la imagen nuevamente
                    time.sleep(1)
                    
                # Agrega un retraso
                time.sleep(2)

            print(n) # Un número repetido muchas veces generalmente indica retraso en alguna decisión o un error de detección

        except TypeError or OSError or gw.PyGetWindowException:
            time.sleep(0.01)

if __name__ == "__main__":
    main()