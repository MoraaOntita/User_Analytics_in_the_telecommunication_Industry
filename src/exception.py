import sys  # This imports the sys module which provides access to some variables used or maintained by the Python interpreter.

from src.logger import logging  # This imports the logging module from src.logger package.

def error_message_detail(error, error_detail:sys):  
    """
    This function takes an error message and error details and constructs a formatted error message 
    with information about where the error occurred in the Python script.
    
    Args:
        error: The error message.
        error_detail: The error details including information about the exception.

    Returns:
        A formatted error message including file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Retrieves the traceback object from the error details.
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extracts the filename where the error occurred.
    # Constructs the error message with file name, line number, and error description.
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message


class CustomException(Exception):
    """
    Custom exception class that extends the built-in Exception class.
    """

    def __init__(self, error_message, error_detail:sys):
        """
        Initializes the CustomException object.
        
        Args:
            error_message: The error message to be displayed.
            error_detail: The error details including information about the exception.
        """
        super().__init__(error_message)  # Calls the constructor of the parent class (Exception) with the error message.
        # Constructs the detailed error message using the provided error message and details.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        """
        String representation of the CustomException object.
        
        Returns:
            The detailed error message.
        """
        return self.error_message

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
