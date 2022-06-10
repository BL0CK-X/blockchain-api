
class Error:

    def __init__(self, error_message, error_code=400):
        self.__error_message = error_message
        self.__error_code = error_code

    def get_error(self):
        return self.__error_message

    def get_error_code(self):
        return self.__error_code
