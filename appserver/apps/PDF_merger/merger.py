from io import BytesIO

import PyPDF2 as p

def merger(file1, file2):
    pdf_merger = p.PdfMerger()
    output = BytesIO()
    try:
        pdf_merger.append(file1)
        pdf_merger.append(file2)
        pdf_merger.write(output)
    finally:
        pdf_merger.close()

    output.seek(0)
    return output
