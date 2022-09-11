
from pynput import keyboard
from pynput.keyboard import Controller, Listener, Key
import time
import random 
_list = []
c = Controller()
COMBINATION = {keyboard.Key.shift, keyboard.Key.enter}
current = set()
curse_words = ['noob', 'manco', 'pinche', 'retrasado', 'marica', 'estupido', 'idiota', 'novato', 'tonto']
responses_allchat = ['Si todos nos llevamos bien el mundo sera un lugar mejor ', 'Tengamos un buen juego amigos los pinches amo', 'na na na na nana na na lider', 'Disfrutemos el juego y demos lo mejor de nosotros mismos ']
responses_curses = ['I love the cock', 'Soy una persona muy insegura por eso iva a insultarlos', 'El tamaño de mi miembro reproductivo es microscopico', 'Si perdiera peso tal ves estaria menos enojado con la vida']

# The currently active modifiers



def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


def press(key):
    

    flag = False
      
    if key in COMBINATION:
        current.add(key)
        flag = True
        if all(k in current for k in COMBINATION):

            if flag == True:
                       
                time.sleep(.2)           
                
                c.type(random.choice(responses_allchat))
                flag = False
                c.release(keyboard.Key.shift)
                time.sleep(.2)
                c.press(keyboard.Key.enter)
            
                c.release(keyboard.Key.enter)
                
                            
                

        
    

    try:
        print(_list, 'pressed')
        if key is not keyboard.Key.space:
            _list.append(key.char)         # <-- Note: key.char
        elif keyboard.Key.space is key: 
            pass
        elif keyboard.Key.enter is key:
            pass
    except AttributeError:
        
        pass
  
def release(key):
    try:
        current.remove(key)
      
            
    except KeyError:
        pass
    
    if key == keyboard.Key.f1:
        # Stop listener
        return False

    if key == keyboard.Key.space:
        word = ''.join(_list)        
        print(word)
        word_count = len(word)
        size= 0
        if word in curse_words:
            while size <= word_count:
                c.press(keyboard.Key.backspace)
                c.release(keyboard.Key.backspace)
                size += 1 

            c.type(random.choice(responses_curses))
            c.press(keyboard.Key.enter)
            c.release(keyboard.Key.enter)   
        _list.clear()

    elif key == keyboard.Key.enter:
        word = ''.join(_list)        
        print(word)
            
        if word in curse_words:
            c.press(keyboard.Key.enter)
            c.release(keyboard.Key.enter)
            time.sleep(.2)
            c.type("no quise decir eso lo siento estoy teninedo un mal dia")
            c.press(keyboard.Key.enter)
            c.release(keyboard.Key.enter)
        _list.clear()

    
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()