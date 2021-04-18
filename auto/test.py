from autoclick import *

click_thread = AutoClick(0.01, Button.left)
click_thread.start()

def on_press(key):
    print(key)
    if key == KeyCode(char='1'):
        click_thread.start_clicker()
        print("AutoMouse Start!")
    elif key == KeyCode(char='2'):
        click_thread.stop_clicker()
        print("AutoMouse Stop!")
    elif key == KeyCode(char='3'):
        click_thread.exit()
        print("AutoMouse Exit!")
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()