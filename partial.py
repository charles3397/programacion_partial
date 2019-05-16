#!/usr/bin/python



import os
import sys 
import classes

a = classes.pagina(4)
b = classes.pagina(4)
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
doc = classes.documento()
doc.add_pagina(a)
doc.add_pagina(a)
doc.add_pagina(a)
doc.add_pagina(a)
doc.insert_pagina(b,2)
doc.eliminate_pagina(3)
doc.export_doc("export.txt")
doc2 = classes.documento()
doc2.import_doc("export.txt")


doc.print_documento()
doc2.print_documento()
