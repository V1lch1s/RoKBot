from Clicks import *

def reintegrarTropas(n):
    # Lista de posibles tropas curadas hasta el momento
    posibleTroopers = [
        './screenshots/Tropas_reintegrar.jpg',
        './screenshots/Tropas_reintegrar_2.jpg',
        './screenshots/Tropas_reintegrar_3.jpg',
        './screenshots/Tropas_reintegrar_4.jpg',
        './screenshots/Tropas_reintegrar_5.jpg',
        './screenshots/Tropas_reintegrar_6.jpg',
        './screenshots/Tropas_reintegrar_7.jpg',
        './screenshots/Tropas_reintegrar_8.jpg',
        './screenshots/Tropas_reintegrar_9.jpg'
    ]

    for imagen in posibleTroopers:
        ubicacion = pyautogui.locateOnScreen(imagen, confidence = 0.8)
        if ubicacion is not None:
            # Obtiene las coordenadas del centro de la imagen detectada
            x, y, width, height = ubicacion
            center_x = x + width // 2
            center_y = (y + height // 2)
            
            # Mueve el cursor hacia la imagen detectada y realiza un clic
            leftClick(center_x, center_y)

            n += 1 # Para este punto ya se habrá completado 1 iteración
            print(n)
            
            # Agrega un retraso
            time.sleep(1)

    return n

if __name__ == "__main__":
    n = reintegrarTropas()
    print(f"Se completaron {n} iteraciones.")