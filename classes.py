#!/usr/bin/python
import os
import sys 


class pagina :

	def __init__(self,numero):
		self.encabezado = ""
		self.text = []
		self.pie_de_pagina = ""

	def add_encabezado(self,text):
		self.encabezado = text
	
	def add_parrafo(self,text):
		self.text.append(text)
	
	def add_pie_de_pagina(self,text):
		self.pie_de_pagina = text
	
	def change_parrafo(self,indice,text):
		self.text[indice] = text	

	def eliminate_parrafo(self,indice):
		del self.text[indice]

	def print_parrafo_content(self):
		for i in self.text :
			print i

	def print_pagina(self):
		print
		print self.encabezado
		print
		for i in self.text :
			print i
		print
		print self.pie_de_pagina
		print
		
	def export_pagina(self,name) :
		page = open(name,"a")
		tmp = "$$".join(self.text)
		tmp = self.encabezado + "///" + tmp +"///" + self.pie_de_pagina + "///"  +"\n"	
		page.write(tmp)
		page.close


	def import_pagina(self,ligne) :
		tmp_thirdpart = ligne.split("///")
		tmp_text = tmp_thirdpart[1].split("$$")
		self.encabezado = tmp_thirdpart[0]
		self.pie_de_pagina = tmp_thirdpart[2]
		self.text = tmp_text	 
		

class documento :
	
	def __init__(self):
		self.nb_paginas = 0
		self.paginas = []

	def add_pagina(self,page):
		self.paginas.append(page)
		self.nb_paginas += 1 

	def print_documento(self) :
		index = 1		
		for i in self.paginas :
			print "pagina ", index," : "
			i.print_pagina()
			index += 1	

	def insert_pagina(self,page,insert):
		self.paginas.insert(insert,page)

	def eliminate_pagina(self,indice):
		del self.paginas[indice]
	
	def change_parrafo(self,parafo,text):
		self.change_parrafo(parafo,text)

	def export_doc(self,name):
		for i in self.paginas :
			i.export_pagina(name)
	
	def import_doc(self,path):
		fil = open(path,"r")
		tmp = fil.readlines()
		for i in tmp :
			page = pagina(0)
			page.import_pagina(i)
			self.add_pagina(page)
		fil.close()
		
		

a = pagina(4)
b = pagina(4)
a.add_encabezado("head")
a.add_parrafo("ku")
a.add_parrafo("ku")
a.add_parrafo("ku")
a.add_pie_de_pagina("pie")
b.add_encabezado("head")
b.add_parrafo("b")
b.add_parrafo("b1")
b.add_parrafo("b")
b.eliminate_parrafo(0)
b.add_pie_de_pagina("pie")
a.print_pagina()
doc = documento()
doc.add_pagina(a)
doc.add_pagina(a)
doc.add_pagina(a)
doc.add_pagina(a)
doc.insert_pagina(b,2)
doc.eliminate_pagina(3)
doc.export_doc("export.txt")
doc2 = documento()
doc2.import_doc("export.txt")
print "2"

#doc.paginas[0].change_parrafo(1,"test_change")

doc.print_documento()
doc2.print_documento()



