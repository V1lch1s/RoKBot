import keyboard
import pywintypes
import pygetwindow as gw
from Clicks import *

def main():
    n = 0 # Bárbaros Masacrados
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

                # Regresa a la Aldea
                if pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.9) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.9)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)    

            # Vamos al mapa si las tropas están listas
            if pyautogui.locateOnScreen('./screenshots/Map.jpg', confidence = 0.8) != None \
                and pyautogui.locateOnScreen('./screenshots/Tropas_curar.jpg', confidence = 0.8) == None \
                and pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8) == None \
                and pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8) == None \
                and pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8) == None:

                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Map.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso
                time.sleep(1)

                # Le damos en buscar
                if pyautogui.locateOnScreen('./screenshots/Buscar.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Buscar.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                    # Click en el botón "Buscar"
                    if pyautogui.locateOnScreen('./screenshots/Boton_buscar.jpg', confidence = 0.8) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('./screenshots/Boton_buscar.jpg', confidence = 0.8)
                        center_x = x + width // 2
                        center_y = (y + height // 2)
                        
                        # Mueve el cursor hacia la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso
                        time.sleep(1)

                    # Hacemos Click en los Bárbaros
                    # (Deben ser mayor a nivel 6 debido a que este es el nivel máximo de los lugares de recolección)
                    while pyautogui.locateOnScreen('./screenshots/Barbaros_niv13.jpg', confidence = 0.9) == None \
                        and keyboard.is_pressed("Esc") != True:
                        print("Ciclo Barbaros_niv13")                    
                        pass

                    if pyautogui.locateOnScreen('./screenshots/Barbaros_niv13.jpg', confidence = 0.9) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('./screenshots/Barbaros_niv13.jpg', confidence = 0.9)
                        center_x = x + width // 2
                        center_y = (y + height // 2)
                        
                        # Mueve el cursor hacia la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso
                        time.sleep(1)

                # Hacemos Click en Atacar
                if pyautogui.locateOnScreen('./screenshots/Atacar.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Atacar.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                # Click en "Tropas Nuevas"
                if pyautogui.locateOnScreen('./screenshots/Tropas_nuevas.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_nuevas.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                # Click en "Marcha"
                if pyautogui.locateOnScreen('./screenshots/Marcha.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Marcha.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                # Regresamos a la Aldea
                if pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Back.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                    # Mientras no se detecte la imagen "Tropas_regresando.jpg" o "Tropas_derrotadas.jpg" se sigue buscando
                    while pyautogui.locateOnScreen('./screenshots/Tropas_regresando.jpg', confidence = 0.8) == None \
                        and pyautogui.locateOnScreen('./screenshots/Tropas_derrotadas.jpg', confidence = 0.8) == None \
                        and keyboard.is_pressed("Esc") != True:
                        print("Atacando Bárbaros")
                        # Se aprovecha el ciclo para detectar si hay acciones realizables dentro de la aldea
                        # Mejora disponible
                        if pyautogui.locateOnScreen('./screenshots/Mejora_disponible.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejora_disponible.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)

                            # Click Mejorar
                            if pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8) != None:
                                # Obtiene las coordenadas del centro de la imagen detectada
                                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8)
                                center_x = x + width // 2
                                center_y = (y + height // 2)
                                
                                # Mueve el cursor hacia la imagen detectada y realiza un clic
                                leftClick(center_x, center_y)
                                
                                # Agrega un retraso
                                time.sleep(1)

                        if pyautogui.locateOnScreen('./screenshots/Mejora_disponible2.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejora_disponible2.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)
                            
                            # Click en el botón de mejora
                            if pyautogui.locateOnScreen('./screenshots/Boton_Mejora.jpg', confidence = 0.8) != None:
                                # Obtiene las coordenadas del centro de la imagen detectada
                                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Boton_Mejora.jpg', confidence = 0.8)
                                center_x = x + width // 2
                                center_y = (y + height // 2)
                                
                                # Mueve el cursor hacia la imagen detectada y realiza un clic
                                leftClick(center_x, center_y)
                                
                                # Agrega un retraso
                                time.sleep(1)

                            # Click Mejorar
                            if pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8) != None:
                                # Obtiene las coordenadas del centro de la imagen detectada
                                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8)
                                center_x = x + width // 2
                                center_y = (y + height // 2)
                                
                                # Mueve el cursor hacia la imagen detectada y realiza un clic
                                leftClick(center_x, center_y)
                                
                                # Agrega un retraso
                                time.sleep(1)

                        # Pedir Ayuda
                        if pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)

                        # Si podemos reintegrar las tropas, lo hacemos
                        if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)

                            n += 1 # Para este punto ya se habrá completado 1 iteración
                            print(n)
                            
                            # Agrega un retraso
                            time.sleep(1)

                        if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)

                            n += 1 # Para este punto ya se habrá completado 1 iteración
                            print(n)
                            
                            # Agrega un retraso
                            time.sleep(1)
                            
                        if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)

                            n += 1 # Para este punto ya se habrá completado 1 iteración
                            print(n)
                            
                            # Agrega un retraso
                            time.sleep(1)

            # Curamos nuestras tropas
            if pyautogui.locateOnScreen('./screenshots/Tropas_curar.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_curar.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso
                time.sleep(1)

                # Click Sanar
                if pyautogui.locateOnScreen('./screenshots/Sanar.jpg', confidence = 0.8) != None:
                    # Obtiene las coordenadas del centro de la imagen detectada
                    x, y, width, height = pyautogui.locateOnScreen('./screenshots/Sanar.jpg', confidence = 0.8)
                    center_x = x + width // 2
                    center_y = (y + height // 2)
                    
                    # Mueve el cursor hacia la imagen detectada y realiza un clic
                    leftClick(center_x, center_y)
                    
                    # Agrega un retraso
                    time.sleep(1)

                # Mientras no se detecta que las tropas están listas, no se avanza
                while pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8) != None \
                    or pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8) != None \
                    or pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8) != None \
                    and keyboard.is_pressed("Esc") != True:
                    
                    # Se aprovecha el ciclo para detectar si hay acciones realizables dentro de la aldea
                    # Mejora disponible
                    if pyautogui.locateOnScreen('./screenshots/Mejora_disponible.jpg', confidence = 0.8) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejora_disponible.jpg', confidence = 0.8)
                        center_x = x + width // 2
                        center_y = (y + height // 2)
                        
                        # Mueve el cursor hacia la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso
                        time.sleep(1)

                        # Click Mejorar
                        if pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)

                    if pyautogui.locateOnScreen('./screenshots/Mejora_disponible2.jpg', confidence = 0.8) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejora_disponible2.jpg', confidence = 0.8)
                        center_x = x + width // 2
                        center_y = (y + height // 2)
                        
                        # Mueve el cursor hacia la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso
                        time.sleep(1)
                        
                        # Click en el botón de mejora
                        if pyautogui.locateOnScreen('./screenshots/Boton_Mejora.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Boton_Mejora.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)

                        # Click Mejorar
                        if pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8) != None:
                            # Obtiene las coordenadas del centro de la imagen detectada
                            x, y, width, height = pyautogui.locateOnScreen('./screenshots/Mejorar.jpg', confidence = 0.8)
                            center_x = x + width // 2
                            center_y = (y + height // 2)
                            
                            # Mueve el cursor hacia la imagen detectada y realiza un clic
                            leftClick(center_x, center_y)
                            
                            # Agrega un retraso
                            time.sleep(1)

                    # Pedir Ayuda
                    if pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8) != None:
                        # Obtiene las coordenadas del centro de la imagen detectada
                        x, y, width, height = pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8)
                        center_x = x + width // 2
                        center_y = (y + height // 2)
                        
                        # Mueve el cursor hacia la imagen detectada y realiza un clic
                        leftClick(center_x, center_y)
                        
                        # Agrega un retraso
                        time.sleep(1)

            # Pedimos ayuda del clan
            if pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Ayuda.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)
                
                # Agrega un retraso
                time.sleep(1)

            # Reintegramos nuestras tropas
            if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

                n += 1 # Para este punto ya se habrá completado 1 iteración
                print(n)
                
                # Agrega un retraso
                time.sleep(1)

            if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_2.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

                n += 1 # Para este punto ya se habrá completado 1 iteración
                print(n)
                
                # Agrega un retraso
                time.sleep(1)
                
            if pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8) != None:
                # Obtiene las coordenadas del centro de la imagen detectada
                x, y, width, height = pyautogui.locateOnScreen('./screenshots/Tropas_reintegrar_3.jpg', confidence = 0.8)
                center_x = x + width // 2
                center_y = (y + height // 2)
                
                # Mueve el cursor hacia la imagen detectada y realiza un clic
                leftClick(center_x, center_y)

                n += 1 # Para este punto ya se habrá completado 1 iteración
                print(n)
                
                # Agrega un retraso
                time.sleep(1)

        except TypeError or OSError or gw.PyGetWindowException:
            time.sleep(0.01)

if __name__ == "__main__":
    main()