class Es(BaseException):
    def __init__(self, code, message):
        self.code = code
        self.message = message
