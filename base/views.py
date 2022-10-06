from django.shortcuts import HttpResponse, render
from base.apps import write_pdf
import os

DIR_BASE = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(DIR_BASE, 'static\\files\\NEO1_form.pdf')
OUTPUT_PATH = os.path.join(DIR_BASE, 'static\\files\\NEO1_edit.pdf')


def home(request):
    return render(request, 'base/home.html')


def respostas_teste(request):
    data_dict = {
        'row_1': request.POST.get('row1'),
        'row_2': request.POST.get('row2'),
        'row_3': request.POST.get('row3'),
        'row_4': request.POST.get('row4'),
        'row_5': request.POST.get('row5'),
    }
    write_pdf(TEMPLATE_PATH, OUTPUT_PATH, data_dict)
    print(data_dict)
    return render(request, 'respostas_teste.html', context=data_dict)
