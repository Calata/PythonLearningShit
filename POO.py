class Cuadrado:
	def cal_area():
		lado = 5
		area = lado*lado
		print "El area es %d"%area
class Nuevo_Contador(contador):
	def __init__ (self, base= 0):
		self.veces = int(base)
	def __int__(self):
		return self.veces
	def __str__(self):
		return str(self.veces):
	def __cmp__ (self,otro):
		return self.veces = otro

Objeto = Cuadrado
Objeto.cal_area()