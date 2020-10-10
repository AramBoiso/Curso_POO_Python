class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password


class Cliente (User):

    def __init__(self, email, password, auto):
        super().__init__(email, password)
        self.auto = auto
    

email = input('Enter your email: ')
password = input('Enter your password: ')
auto = input('Enter your auto: ')

cliente = Cliente(email, password, auto)

print('Email: {} \nPassword: {} \nAutomovil: {}'.format(getattr(cliente, 'email'), getattr(cliente, 'password'), getattr(cliente, 'auto')))