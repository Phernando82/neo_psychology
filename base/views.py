import os
from django.shortcuts import HttpResponse, render
from base.apps import write_pdf

DIR_BASE = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(DIR_BASE, 'static\\files\\neo_form.pdf')
OUTPUT_PATH = os.path.join(DIR_BASE, 'static\\files\\neo_resp.pdf')


def home(request):
    return render(request, 'base/home.html')


def page1(request):
    return render(request, 'page1.html')


def respostas_teste(request):
    data_dict = {
        'row_1': request.POST.get('row1'),
        'row_2': request.POST.get('row2'),
        'row_3': request.POST.get('row3'),
        'row_4': request.POST.get('row4'),
        'row_5': request.POST.get('row5'),
        'row_6': request.POST.get('row6'),
        'row_7': request.POST.get('row7'),
        'row_8': request.POST.get('row8'),
        'row_9': request.POST.get('row9'),
        'row_10': request.POST.get('row10'),
        'row_11': request.POST.get('row11'),
        'row_12': request.POST.get('row12'),
        'row_13': request.POST.get('row13'),
        'row_14': request.POST.get('row14'),
        'row_15': request.POST.get('row15'),
        'row_16': request.POST.get('row16'),
        'row_17': request.POST.get('row17'),
        'row_18': request.POST.get('row18'),
        'row_19': request.POST.get('row19'),
        'row_20': request.POST.get('row20'),
        'row_21': request.POST.get('row21'),
        'row_22': request.POST.get('row22'),
        'row_23': request.POST.get('row23'),
        'row_24': request.POST.get('row24'),
    }
    write_pdf(TEMPLATE_PATH, OUTPUT_PATH, data_dict)
    print(data_dict)
    return render(request, 'respostas_teste.html', context=data_dict)


def download_pdf_file(request):
    file_name = 'neo_resp.pdf'
    # Defina o caminho completo do arquivo
    path_file = DIR_BASE + '/static/files/' + file_name
    response = HttpResponse(open(path_file, 'rb').read())
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = "attachment; file_name =% s " % file_name
    return response
