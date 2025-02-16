import PyPDF2


#PARA ABRIR EL ARCHIVO PDF
pdf = open('Guia de Auditoria GAT V. 4.0 - 2024.pdf','rb')

reader = PyPDF2.PdfReader(pdf)

##SE PONE A ITERAR TODAS LA PAGINAS 
for no_page in range(len(reader.pages)):
    print('Pagina', no_page+1)
    info_page=reader._get_page(no_page)
    ###SE EXTRAE LA INFORMACION DESDE EL DOCUMENTO 
    extract_info = info_page.extract_text()
    ###SE IMPRIME LA VARIABLE QUE EXTRAE EL TEXTO 
    print(extract_info)
    print('*************')
