##any exception has been controll sys lib has already being present
import sys 
from src.logger import logging

def err_msg_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in a py script [{0}] line no. [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=err_msg_detail(error_message,error_detail=error_detail)

    def __str_(self):
        return self.error_message
    
#     # Example usage
# if __name__=="__main__":
#    try:
#     # Some code that might raise an exception
#        x = 1 / 0
#    except Exception as e:
#        logging.info("mathematical error has occured ")
#        raise CustomException(e,sys)