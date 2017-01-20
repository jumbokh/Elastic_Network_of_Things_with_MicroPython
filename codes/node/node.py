# coding: utf-8

import os
import sys

if not sys.implementation.name == 'micropython':
    sys.path.append(os.path.abspath(os.path.join(os.path.pardir, 'shared')))
        
import config
import commander


if config.IS_MICROPYTHON:
    import worker_upython as worker_impl
else:
    import worker_cpython as worker_impl   
    

class Node(commander.Commander):

    def __init__(self):
        super().__init__()
        self.worker = worker_impl.Worker(config.BROKER_HOST, config.HUB_PORT)
        self.worker.set_parent(self)
        
        
    def __del__(self):
        self.stop()
        
        
    def set_default_code_book(self):
        code_book = {}
        self.set_code_book(code_book) 
        
            
    def run(self): 
        self.worker.run()
 
 
    def stop(self): 
        self.worker.stop()
        self.worker.set_parent(None)
        del self.worker
        
        
    def request(self, **message):
        self.worker.request(message)
        
        

def main():
    try:
        node = Node()
        node.run() 
        
    except KeyboardInterrupt:
        print("Ctrl C - Stopping.")
        sys.exit(1)            
                
        
if __name__ == '__main__':
    main()
        


