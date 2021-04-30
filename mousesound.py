from pynput import mouse
import simpleaudio as sa
import random

file_numbers = [11]
sounds = [sa.WaveObject.from_wave_file(f"{n}.wav") for  n in file_numbers]

class StopListener(Exception):
    def __init__(self, message):
        self.message = message

stop_count = 1
def on_click(x, y, button, pressed):
    global stop_count
    if button == mouse.Button.x2:
        if stop_count > 1:
            raise StopListener("Stopped by you.")
        stop_count += 1
    else:
        stop_count = 0
    
    icon = "🦀" if button == mouse.Button.left else "🦐"
    if not pressed: 
        icon = "  " + icon

    sound = random.choice(sounds)
    sound.play()

    print("\r   ", end="")
    print(f"\r{icon}", end="")

print("Let's kani dance.")
with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except StopListener as e:
        print(e.message)
