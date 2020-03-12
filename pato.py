class nombre_user():
	def __init__(self,nombre, apellido, mail):
		self.nombre = nombre		
		self.apellido = apellido
		self.mail = mail
	
	def print_nombre(self):
		print(self.nombre)
	def print_apellido(self):
		print(self.apellido)
	def print_mail(self):
		print(self.mail)
		
listaUsuario = list()
def mostrarMenu():
	print("1. Registrar usuario")
	print("2. Mostrar usuario")
	print("3. Salir")
while True:
	mostrarMenu()
	opc = input()
	if opc == "1":
		print("Ingrese su nombre")
		nombre = input()
		print("Ingrese su apellido")
		apellido = input()
		print("Ingrese su correo electronico")
		mail = input()
		persona = nombre_user(nombre, apellido, mail)
		listaUsuario.append(persona)
