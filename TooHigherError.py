class TooHigherError(Exception):
    def __init__(self, message='the salary is higher than 100k'):
        self.message = message

    def __str__(self):
        return f'TooHigherError: {self.message}'
    