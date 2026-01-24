import logging
#logging.basicConfig(level=logging.WARNING) #warning eka saha ita wada wadi level wala ewa pennanne
#logging.basicConfig(level=logging.WARNING,format="%(asctime)s-%(levelname)s-%(message)s") #methana format ekata denna puluwan attribute okkoma documantation eke thiynwa balanna
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s",filename="log.py") #file ekakata save karannwa

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")

