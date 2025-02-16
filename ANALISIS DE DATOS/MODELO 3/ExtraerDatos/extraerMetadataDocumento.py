import PyPDF2


#PARA ABRIR EL ARCHIVO PDF
pdf = open('Guia de Auditoria GAT V. 4.0 - 2024.pdf','rb')

reader = PyPDF2.PdfReader(pdf)


####CODIGO PARA BUSCAR METADATOS 
meta = reader.metadata

###IMPRIMIR EL DATO DEL METADATO QUE SE DESEA CONOCER 
print(meta.producer)