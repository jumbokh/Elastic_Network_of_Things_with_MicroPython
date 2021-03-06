# coding: utf-8


import time
# noinspection PyUnresolvedReferences
import worker
# noinspection PyUnresolvedReferences
import led
# noinspection PyUnresolvedReferences
import u_python


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyPep8Naming
class Worker(worker.Worker):
        
    # Object control
    # @profile(precision=4)
    def __init__(self, server_address, server_port):
        super().__init__(server_address, server_port)
        self.now = time.ticks_ms
        
        
    # code book_______________________
    # @profile(precision=4)
    def set_default_code_book(self):
        code_book = {'read GPIOs': self.read_GPIOs,
                     'write GPIOs': self.write_GPIOs,
                     'blink led': self.blink_led}      
        self.set_code_book(code_book)        
        
        
    # @profile(precision=4)
    def rename(self, name):
        self.name = name
        
        
    # Specialized functions__________
    def read_GPIOs(self, pins):
        return u_python.read_GPIOs_pins(pins)
        

    # @profile(precision=4)
    def write_GPIOs(self, pins_and_values): 
        return u_python.write_GPIOs_pins(pins_and_values)
        
    
    # @profile(precision=4)
    def blink_led(self, times = 1, forever = False, on_seconds = 0.5, off_seconds = 0.5):
        led.blink_on_board_led(times = times, 
                               forever = forever,
                               on_seconds = on_seconds,
                               off_seconds = off_seconds)
