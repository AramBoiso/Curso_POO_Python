#Clase
#self hace referencia al objeto
class User:

    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.age = None

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    

#objeto    
usuario = User()

us = usuario.username = 'aram_boiso'
e = usuario.email = 'aramboisso@gmail.com'
usuario.setPassword('micontra1234')

print(f'\nUsuario: {us} \nCorreo: {e} \nContraseña: { usuario.getPassword() }')

#Metodos aprendidos 

setattr(usuario, 'username', 'missa_19')
setattr(usuario, 'email', 'missa_19@email.com')
setattr(usuario, 'password', 'newPass123')

print(f'\nUsuario: { getattr(usuario, "username") } \nCorreo: { getattr(usuario, "email") } \nContraseña: {getattr(usuario, "password")}')

print(f'\nedad ?: {hasattr(usuario, "age")}')




