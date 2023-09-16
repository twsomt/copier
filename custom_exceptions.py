class MissingVariable(Exception):
    '''Срабатывает, когда отсутствует одна из переменных окружения .env'''

    def __init__(self, variable_name=''):
        self.variable_name = variable_name

    def __str__(self):
        return f'Переменная {self.variable_name} отсутствует в файле .env'
