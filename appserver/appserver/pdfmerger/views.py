from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import time
import datetime
from apps.PDF_merger.merger import merger as merge_files
# Create your views here.
def merger(request):
    return render(request, 'pdfmerger/index.html')

def merge_pdfs(request):
    if request.method == 'POST':
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')

        if file1 and file2:
            inicio = time.perf_counter()
            merged_pdf = merge_files(file1, file2)
            duracao = time.perf_counter() - inicio
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            response = FileResponse(merged_pdf, as_attachment=True, filename=f'merged_{timestamp}.pdf', content_type='application/pdf')
            print(f"Tempo de execução: {duracao:.4f} segundos")
            return response

    return render(request, 'pdfmerger/index.html', {'error': 'Please upload two PDF files.'})