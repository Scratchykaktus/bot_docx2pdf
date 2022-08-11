from docx2pdf import convert
import os

def conv(fname):
    path_doc_files = 'files/convert_files'
    path_pdf_files = 'files/convert_files/success'

    path_folder = os.listdir(path_doc_files)

    file_name, file_expansion = os.path.splitext(fname)

    if fname in path_folder and file_expansion == '.docx':
        convert(f'{path_doc_files}/{fname}', f"{path_pdf_files}/{file_name}.pdf")
        return f"{path_pdf_files}/{file_name}.pdf"
    else:
        raise NameError

    
