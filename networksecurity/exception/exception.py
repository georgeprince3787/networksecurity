import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
        # Log the exception
        logger.error(f"Exception: {self.error_message} at {self.file_name}:{self.lineno}")

    def __str__(self):
        return "Error occured in script: [{0}] at line number: [{1}] error message: [{2}]".format(self.file_name,self.lineno,self.error_message)


if __name__ == "__main__":
    try:
        logger.info("Enter the try block")
        a = 1/0
        print("This will not be printed",a)
    except Exception as ex:
        logger.error(f"Exception caught in except block: {str(ex)}")
        raise NetworkSecurityException(ex,sys)