import subprocess

#///////////////////////////////////////////////////CLASE RamaArbol//////////////////////////////////////////////////////////////////////////////////////////////''

class RamaArbol(object):
	def __init__(self):
		self.cadena = None
		self.tempFlechas = None

	def ramaArbol(self):
		self.cuenta = 0
		self.hoja = True

	def insertar(self, nodo = None):
		if estaEnBlanco():
			primero = nodo
			primero.setAnterior(None)
			primero.setSiguiente(None)
			self.cuenta += 1

		else:
			temp = primero
			if  nodo.getCodigoTransaccion() == temp.getCodigoTransaccion():
				return
			elif nodo.getCodigoTransaccion() < temp.getCodigoTransaccion():
				self.cuenta += 1
			if temp == primero:
				primero.setAnterior(nodo)
				primero.setIzquierda(nodo.getDerecha())
				nodo.setSiguiente(primero)
				primero = nodo
				return
			elif temp.getSiguiente() is None:
				self.cuenta += 1
				temp.setSiguiente(nodo)
				temp.setDerecha(nodo.getIzquierda())
				nodo.setAnterior(temp)
				nodo.setSiguiente(None)
				return
			else:
				nodo.setAnterior(temp.setAnterior())
				nodo.setSiguiente(temp)
				temp.getAnterior().setSiguiente(nodo)
				temp.getAnterior().setDerecha(nodo.getIzquierda())
				temp.setAnterior(nodo)
				temp.setIzquierda(nodo.getDerecha())
				return 

				temp = temp.getSiguiente()
	def getCuenta(self):
		return self.cuenta 

	def estaEnBlanco(self):
		return self.primero == None

	def getPrimero(self):
		return self.primero

	def setPrimero (self,primero):
		self.primero = primero 

	def esHoja(self):
		return self.hoja

	def setHoja(self, hoja):
		self.hoja = hoja 

	def getGraphNodo(self):
		tempFlechas = None
		temp = "nodo" + primero.getCodigoTransaccion() + " [ label =\""
		tempRecorre = primero 
		self.i = 0
		detalles = None
		for cuenta in tempRecorre.getSiguiente():
			cadena = cadena + tempRecorre.getCodigoActivo().ToString() + ","
			cadena = cadena + tempRecorre.getCodigoTransaccion().ToString() + ","
			cadena = cadena + ";"
			temp += "<C" + i + ">|<D" + i + ">ID-TRANS: " + tempRecorre.getCodigoTransaccion() + "\\nCOD_ACTI: " + tempRecorre.getCodigoActivo() +  "|"
			temp += "<C" + i + ">|<D" + i + ">ID-TRANS: " + tempRecorre.getCodigoTransaccion() + "\\nCOD_ACTI: " + tempRecorre.getCodigoActivo() +  "|"
		if tempRecorre.getIzquierda() is not None:
			tempFlechas += "nodo" + primero.getCodigoTransaccion() + ":C" + i + "->nodo" + tempRecorre.getIzquierda().primero.getCodigoTransaccion() + "\n"

			
			temp += "<C" + i + ">\" fillcolor=\"#CCCCCC\"];\n"
			tempRecorre = primero
			while tempRecorre.getSiguiente() is not None:
				tempRecorre = tempRecorre.getSiguiente()
		if tempRecorre.getDerecha() is not None:
			tempFlechas += "nodo" + primero.getCodigoTransaccion() + ":C" + i + "->nodo" + tempRecorre.getDerecha().primero.getCodigoTransaccion() + "\n"

		temp += tempFlechas;
		temp += detalles;
   
	   
		return temp;
		

#///////////////////////////////////////////////////FINAL CLASE RamaArbol//////////////////////////////////////////////////////////////////////////////////////'''

class NodoRamaArbol(object):
	def __init__ (self):

		codigoTransaccion = ""
		codigoActivo = ""


	def NodoRamaArbol (self, codigoTransaccion, codigoActivo):
		self.codigoTransaccion = codTrans
		self.codigoActivo = codActi
#///////////////////////////////////////////////////CODIGO DE TRANSACCION///////////////////////////////////////////////////////////////////'''
	def  getCodigoTransaccion(self):
		return codigoTrans

	def setCodigoTransaccion(codTransacc):
		self.codigoTrans = codTransacc
#///////////////////////////////////////////////////FINAL CODIGO TRANSACCION///////////////////////////////////////////////////////////////////'''


#///////////////////////////////////////////////////CODIGO ACTIVO///////////////////////////////////////////////////////////////////'''

	def  getCodigoActivo(self):
		return codActi

	def setCodigoActivo(codActivi):
		self.codActi = codActivi
#///////////////////////////////////////////////////FINAL CODIGO ACTIVO///////////////////////////////////////////////////////////////////'''

		
#///////////////////////////////////////////////////PUNTEROS///////////////////////////////////////////////////////////////////'''

	def getAnterior():
		return self.anterior

	def setAnterior(self, anterior):
		self.anterior = anterior 

	def getSiguiente():
		return self.siguiente

	def setSiguiente(self, siguiente):
		self.siguiente = siguiente 

	
	def getDerecha():
		return self.derecha

	def setDerecha(self, derecha):
		self.derecha = derecha

	def getIzquierda():
		return self.izquierda

	def setIzquierda(self, izquierda):
		self.izquierda = izquierda
#///////////////////////////////////////////////////FINAL PUNTEROS///////////////////////////////////////////////////////////////////'''

#///////////////////////////////////////////////////FINAL CLASE NODORAMA ARBOL///////////////////////////////////////////////////////////////////'''








#/////////////////////////////////////////////////// CLASE MAIN //////////////////////////////////////////////////////////////////////////////////////////'''
		def report(self):
		if self.head is None:
			return

		buffer = self.head
		report = open('Graphs/SimpleListReport.dot', 'w+')
		report.write("digraph SimpleList{\n\t\"" + str(buffer) + "\"[label=\"" + str(buffer) + "\"]\n")
		while buffer.right is not None:
			report.write("\t\"" + str(buffer.right) + "\"[label=\"" + str(buffer.right) + "\"]\n")
			report.write("\t\"" + str(buffer) + "\"->\"" + str(buffer.right) + "\"\n")
			report.write("\t\"" + str(buffer.right) + "\"->\"" + str(buffer) + "\"\n")
			buffer = buffer.right

		report.write("}")
		report.close()
		gen = open('Graphs/gengraph.sh', 'w+')
		gen.write("dot Graphs/SimpleListReport.dot -Tjpg -o Graphs/SimpleList.jpg\n")
		gen.write("xdg-open Graphs/SimpleList.jpg\n")
		gen.close()
		subprocess.call(['./Graphs/gengraph.sh'], shell=True)




			





#/////////////////////////////////////////////////// CLASE MAIN //////////////////////////////////////////////////////////////////////////////////////////'''
