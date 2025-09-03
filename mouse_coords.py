import pyautogui
import time


def get_mouse_position():
    x, y = pyautogui.position()
    return x, y


if __name__ == "__main__":
    print("Posiciona o mouse e espera...")
    time.sleep(3)  # Espera 3 segundos para posicionar o mouse
    x, y = get_mouse_position()
    print(f"As coordenadas obtidas são: X={x}, Y={y}")