import PyPDF2

reader = PyPDF2.PdfFileReader(
    open('1 Goals_of_Caring_for_IBD_patient_FINAL.original.1567699380.pdf', 'rb'))

page = reader.getPage(0)
