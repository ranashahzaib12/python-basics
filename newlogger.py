#to run multiple loggin file we need to Restart the kernel for a new configuration
import logging
#Configuring logging
logging.basicConfig(
    filename='app.log', 
    filemode='w',#Saving all the configuration details in file
    level=logging.DEBUG, 
    format='%(asctime)s=%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
    )
