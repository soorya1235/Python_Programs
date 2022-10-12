import logging
class Charactershouldbeless(ValueError):
    def __init__(self,message):
        self.message = message

logging.basicConfig(filename="test.log",level=logging.DEBUG)
a=10

if a > 5:
    logging.info("test passed")
    raise Charactershouldbeless("It is greater than 5")
else:
    logger.error("test failed")
    print("Correct value is entered")
