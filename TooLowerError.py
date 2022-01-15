class TooLowerError(Exception):
    def __init__(self, message='the salary is lower than 10k'):
        self.message = message

    def __str__(self):
        return f'TooLowerError: {self.message}'