import PyPDF2


#PARA ABRIR EL ARCHIVO PDF
pdf = open('Guia de Auditoria GAT V. 4.0 - 2024.pdf','rb')

reader = PyPDF2.PdfReader(pdf)

####SE LE INDICA LA HOJA QUE DEBE DE EXTRAER

page = reader._get_page(200)

##SE DECLARA UNA VARIABLE SOBRE LA CUAL SE EXTRAE EL TEXTO 

informacion = page.extract_text()

#GUARDAR EL TEXTO EXTRAIDO EN UN ARCHIVO .TXT

with open('info_pdf.txt','w') as txt:
    txt.write(informacion)
