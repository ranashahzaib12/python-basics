
import logging
# Logging setting
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s=%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler("app1.log"),logging.StreamHandler()]
    )

logger=logging.getLogger("AirthmeticAPP")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")    
    return result 

def sub(a,b):
    result = a-b
    logger.debug(f"subing {a} - {b} = {result}")    
    return result

def div(a,b):
    try:
        result = a / b
        logger.debug(f"Dividng {a} / {b} = {result}")    
        return result
    except ZeroDivisionError:
        logger.error("Division by zero Error")
        return None


add(10,33)
sub(55,32)
div(22,0)
