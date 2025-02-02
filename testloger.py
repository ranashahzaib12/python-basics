#By doing this we write in the file automatically the conent of debug 

from newlogger import logging

def add(a,b):
    logging.debug("THis addition ooperation is taking place")
    return a+b

logging.debug('The addition function is  called')
add(10,15)
