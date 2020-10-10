class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

u = User('aramboisso@gamil.com', '1234')

print(getattr(u,'email'))
