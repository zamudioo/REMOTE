from flask import Flask, render_template
from flask_socketio import SocketIO
import pyautogui
import socket

SCROLL_FACTOR = 5  # Ajusta el factor para modificar la velocidad de scroll

app = Flask(__name__)
socketio = SocketIO(app)

# Conjunto de teclas especiales
SPECIAL_KEYS = {
    "esc", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
    "tab", "capslock", "shift", "ctrl", "alt", "win", "menu", "enter", "backspace","space"
}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/mouse')
def mouse():
    return render_template('mouse.html')

@socketio.on('volume')
def handle_volume(data):
    if data == 'up':
        pyautogui.press('volumeup')
    elif data == 'down':
        pyautogui.press('volumedown')
    elif data == 'mute':
        pyautogui.press('volumemute')

@socketio.on('media')
def handle_media(data):
    if data == 'play_pause':
        pyautogui.press('playpause')
    elif data == 'next':
        pyautogui.press('nexttrack')
    elif data == 'prev':
        pyautogui.press('prevtrack')

@socketio.on('keyboard')
def handle_keyboard(data):
    key = data.strip()
    if key.lower() in SPECIAL_KEYS:
        pyautogui.press(key.lower())
    else:
        pyautogui.write(key)

@socketio.on('special')
def handle_special(data):
    if data == 'space' :
        pyautogui.press('space')
    elif data == 'esc' :
        pyautogui.press('esc')
    elif data == 'win' :
        pyautogui.press('win')
    elif data == 'up' :
        pyautogui .press('up')
    elif data == 'down' :
        pyautogui .press('down')
    elif data == 'right' :
        pyautogui .press('right')
    elif data == 'left' :
        pyautogui .press('left')
    elif data == 'prtsc' :
        pyautogui .press('prtsc')
    elif data == 'copy' :
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
    elif data == 'paste' :
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
    elif data == 'f1' :
        pyautogui .press('f1')
    elif data == 'f2' :
        pyautogui .press('f2')
    elif data == 'f3' :
        pyautogui .press('f3')
    elif data == 'f4' :
        pyautogui .press('f4')
    elif data == 'f5' :
        pyautogui .press('f5')
    elif data == 'f6' :
        pyautogui .press('f6')
    elif data == 'f7' :
        pyautogui .press('f7')
    elif data == 'f8' :
        pyautogui .press('f8')
    elif data == 'f9' :
        pyautogui .press('f9')
    elif data == 'f10' :
        pyautogui .press('f10')
    elif data == 'f11' :
        pyautogui .press('f11')
    elif data == 'f12' :
        pyautogui .press('f12')
    elif data == 'cap' :
        pyautogui.keyDown('alt')
        pyautogui.press('f1')
        pyautogui.keyUp('alt')
    elif data == 'vid' :
        pyautogui.press('f23')
    

@socketio.on('mouse_move')
def handle_mouse_move(data):
    dx = data.get('dx', 0)
    dy = data.get('dy', 0)
    pyautogui.moveRel(dx, dy)

@socketio.on('mouse_click')
def handle_mouse_click(data):
    button = data.get('button', 'left')
    pyautogui.click(button=button)

@socketio.on('mouse_down')
def handle_mouse_down(data):
    button = data.get('button', 'left')
    pyautogui.mouseDown(button=button)

@socketio.on('mouse_up')
def handle_mouse_up(data):
    button = data.get('button', 'left')
    pyautogui.mouseUp(button=button)

@socketio.on('mouse_scroll')
def handle_mouse_scroll(data):
    raw_dy = data.get('dy', 0)
    try:
        dy = int(raw_dy) * SCROLL_FACTOR
    except (TypeError, ValueError):
        dy = 0
    if dy != 0:
        pyautogui.scroll(dy)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    ip = get_local_ip()
    port = 5000
    print(f'Servidor corriendo en http://{ip}:{port}')
    socketio.run(app, host='0.0.0.0', port=port)
