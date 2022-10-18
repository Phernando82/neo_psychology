import os
from django.shortcuts import HttpResponse, render
from base.apps import write_pdf
from decouple import config

DIR_BASE = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(DIR_BASE, 'static\\files\\neo_form.pdf')
OUTPUT_PATH = os.path.join(DIR_BASE, 'static\\files\\neo_resp.pdf')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)

if AWS_ACCESS_KEY_ID:
    TEMPLATE_PATH = os.path.join(DIR_BASE, 'static/files/neo_form.pdf')
    OUTPUT_PATH = os.path.join(DIR_BASE, 'static/files/neo_resp.pdf')


def home(request):
    return render(request, 'base/home.html')


def page1(request):
    request.session['row_1'] = request.POST.get('row1')
    request.session['row_2'] = request.POST.get('row2')
    request.session['row_3'] = request.POST.get('row3')
    request.session['row_4'] = request.POST.get('row4')
    request.session['row_5'] = request.POST.get('row5')
    request.session['row_6'] = request.POST.get('row6')
    request.session['row_7'] = request.POST.get('row7')
    request.session['row_8'] = request.POST.get('row8')
    request.session['row_9'] = request.POST.get('row9')
    request.session['row_10'] = request.POST.get('row10')
    request.session['row_11'] = request.POST.get('row11')
    request.session['row_12'] = request.POST.get('row12')
    request.session['row_13'] = request.POST.get('row13')
    request.session['row_14'] = request.POST.get('row14')
    request.session['row_15'] = request.POST.get('row15')
    request.session['row_16'] = request.POST.get('row16')
    request.session['row_17'] = request.POST.get('row17')
    request.session['row_18'] = request.POST.get('row18')
    request.session['row_19'] = request.POST.get('row19')
    request.session['row_20'] = request.POST.get('row20')
    request.session['row_21'] = request.POST.get('row21')
    request.session['row_22'] = request.POST.get('row22')
    request.session['row_23'] = request.POST.get('row23')
    request.session['row_24'] = request.POST.get('row24')
    return render(request, 'page1.html')


def page2(request):
    request.session['row_25'] = request.POST.get('row25')
    request.session['row_26'] = request.POST.get('row26')
    request.session['row_27'] = request.POST.get('row27')
    request.session['row_28'] = request.POST.get('row28')
    request.session['row_29'] = request.POST.get('row29')
    request.session['row_30'] = request.POST.get('row30')
    request.session['row_31'] = request.POST.get('row31')
    request.session['row_32'] = request.POST.get('row32')
    request.session['row_33'] = request.POST.get('row33')
    request.session['row_34'] = request.POST.get('row34')
    request.session['row_35'] = request.POST.get('row35')
    request.session['row_36'] = request.POST.get('row36')
    request.session['row_37'] = request.POST.get('row37')
    request.session['row_38'] = request.POST.get('row38')
    request.session['row_39'] = request.POST.get('row39')
    request.session['row_40'] = request.POST.get('row40')
    request.session['row_41'] = request.POST.get('row41')
    request.session['row_42'] = request.POST.get('row42')
    request.session['row_43'] = request.POST.get('row43')
    request.session['row_44'] = request.POST.get('row44')
    request.session['row_45'] = request.POST.get('row45')
    request.session['row_46'] = request.POST.get('row46')
    request.session['row_47'] = request.POST.get('row47')
    request.session['row_48'] = request.POST.get('row48')
    return render(request, 'page2.html')


def page3(request):
    request.session['row_49'] = request.POST.get('row49')
    request.session['row_50'] = request.POST.get('row50')
    request.session['row_51'] = request.POST.get('row51')
    request.session['row_52'] = request.POST.get('row52')
    request.session['row_53'] = request.POST.get('row53')
    request.session['row_54'] = request.POST.get('row54')
    request.session['row_55'] = request.POST.get('row55')
    request.session['row_56'] = request.POST.get('row56')
    request.session['row_57'] = request.POST.get('row57')
    request.session['row_58'] = request.POST.get('row58')
    request.session['row_59'] = request.POST.get('row59')
    request.session['row_60'] = request.POST.get('row60')
    request.session['row_61'] = request.POST.get('row61')
    request.session['row_62'] = request.POST.get('row62')
    request.session['row_63'] = request.POST.get('row63')
    request.session['row_64'] = request.POST.get('row64')
    request.session['row_65'] = request.POST.get('row65')
    request.session['row_66'] = request.POST.get('row66')
    request.session['row_67'] = request.POST.get('row67')
    request.session['row_68'] = request.POST.get('row68')
    request.session['row_69'] = request.POST.get('row69')
    request.session['row_70'] = request.POST.get('row70')
    request.session['row_71'] = request.POST.get('row71')
    request.session['row_72'] = request.POST.get('row72')
    return render(request, 'page3.html')


def page4(request):
    request.session['row_73'] = request.POST.get('row73')
    request.session['row_74'] = request.POST.get('row74')
    request.session['row_75'] = request.POST.get('row75')
    request.session['row_76'] = request.POST.get('row76')
    request.session['row_77'] = request.POST.get('row77')
    request.session['row_78'] = request.POST.get('row78')
    request.session['row_79'] = request.POST.get('row79')
    request.session['row_80'] = request.POST.get('row80')
    request.session['row_81'] = request.POST.get('row81')
    request.session['row_82'] = request.POST.get('row82')
    request.session['row_83'] = request.POST.get('row83')
    request.session['row_84'] = request.POST.get('row84')
    request.session['row_85'] = request.POST.get('row85')
    request.session['row_86'] = request.POST.get('row86')
    request.session['row_87'] = request.POST.get('row87')
    request.session['row_88'] = request.POST.get('row88')
    request.session['row_89'] = request.POST.get('row89')
    request.session['row_90'] = request.POST.get('row90')
    request.session['row_91'] = request.POST.get('row91')
    request.session['row_92'] = request.POST.get('row92')
    request.session['row_93'] = request.POST.get('row93')
    request.session['row_94'] = request.POST.get('row94')
    request.session['row_95'] = request.POST.get('row95')
    request.session['row_96'] = request.POST.get('row96')
    return render(request, 'page4.html')


def page5(request):
    request.session['row_97'] = request.POST.get('row97')
    request.session['row_98'] = request.POST.get('row98')
    request.session['row_99'] = request.POST.get('row99')
    request.session['row_100'] = request.POST.get('row100')
    request.session['row_101'] = request.POST.get('row101')
    request.session['row_102'] = request.POST.get('row102')
    request.session['row_103'] = request.POST.get('row103')
    request.session['row_104'] = request.POST.get('row104')
    request.session['row_105'] = request.POST.get('row105')
    request.session['row_106'] = request.POST.get('row106')
    request.session['row_107'] = request.POST.get('row107')
    request.session['row_108'] = request.POST.get('row108')
    request.session['row_109'] = request.POST.get('row109')
    request.session['row_110'] = request.POST.get('row110')
    request.session['row_111'] = request.POST.get('row111')
    request.session['row_112'] = request.POST.get('row112')
    request.session['row_113'] = request.POST.get('row113')
    request.session['row_114'] = request.POST.get('row114')
    request.session['row_115'] = request.POST.get('row115')
    request.session['row_116'] = request.POST.get('row116')
    request.session['row_117'] = request.POST.get('row117')
    request.session['row_118'] = request.POST.get('row118')
    request.session['row_119'] = request.POST.get('row119')
    request.session['row_120'] = request.POST.get('row120')
    return render(request, 'page5.html')


def page6(request):
    request.session['row_121'] = request.POST.get('row121')
    request.session['row_122'] = request.POST.get('row122')
    request.session['row_123'] = request.POST.get('row123')
    request.session['row_124'] = request.POST.get('row124')
    request.session['row_125'] = request.POST.get('row125')
    request.session['row_126'] = request.POST.get('row126')
    request.session['row_127'] = request.POST.get('row127')
    request.session['row_128'] = request.POST.get('row128')
    request.session['row_129'] = request.POST.get('row129')
    request.session['row_130'] = request.POST.get('row130')
    request.session['row_131'] = request.POST.get('row131')
    request.session['row_132'] = request.POST.get('row132')
    request.session['row_133'] = request.POST.get('row133')
    request.session['row_134'] = request.POST.get('row134')
    request.session['row_135'] = request.POST.get('row135')
    request.session['row_136'] = request.POST.get('row136')
    request.session['row_137'] = request.POST.get('row137')
    request.session['row_138'] = request.POST.get('row138')
    request.session['row_139'] = request.POST.get('row139')
    request.session['row_140'] = request.POST.get('row140')
    request.session['row_141'] = request.POST.get('row141')
    request.session['row_142'] = request.POST.get('row142')
    request.session['row_143'] = request.POST.get('row143')
    request.session['row_144'] = request.POST.get('row144')
    return render(request, 'page6.html')


def page7(request):
    request.session['row_145'] = request.POST.get('row145')
    request.session['row_146'] = request.POST.get('row146')
    request.session['row_147'] = request.POST.get('row147')
    request.session['row_148'] = request.POST.get('row148')
    request.session['row_149'] = request.POST.get('row149')
    request.session['row_150'] = request.POST.get('row150')
    request.session['row_151'] = request.POST.get('row151')
    request.session['row_152'] = request.POST.get('row152')
    request.session['row_153'] = request.POST.get('row153')
    request.session['row_154'] = request.POST.get('row154')
    request.session['row_155'] = request.POST.get('row155')
    request.session['row_156'] = request.POST.get('row156')
    request.session['row_157'] = request.POST.get('row157')
    request.session['row_158'] = request.POST.get('row158')
    request.session['row_159'] = request.POST.get('row159')
    request.session['row_160'] = request.POST.get('row160')
    request.session['row_161'] = request.POST.get('row161')
    request.session['row_162'] = request.POST.get('row162')
    request.session['row_163'] = request.POST.get('row163')
    request.session['row_164'] = request.POST.get('row164')
    request.session['row_165'] = request.POST.get('row165')
    request.session['row_166'] = request.POST.get('row166')
    request.session['row_167'] = request.POST.get('row167')
    request.session['row_168'] = request.POST.get('row168')
    return render(request, 'page7.html')


def page8(request):
    request.session['row_169'] = request.POST.get('row169')
    request.session['row_170'] = request.POST.get('row170')
    request.session['row_171'] = request.POST.get('row171')
    request.session['row_172'] = request.POST.get('row172')
    request.session['row_173'] = request.POST.get('row173')
    request.session['row_174'] = request.POST.get('row174')
    request.session['row_175'] = request.POST.get('row175')
    request.session['row_176'] = request.POST.get('row176')
    request.session['row_177'] = request.POST.get('row177')
    request.session['row_178'] = request.POST.get('row178')
    request.session['row_179'] = request.POST.get('row179')
    request.session['row_180'] = request.POST.get('row180')
    request.session['row_181'] = request.POST.get('row181')
    request.session['row_182'] = request.POST.get('row182')
    request.session['row_183'] = request.POST.get('row183')
    request.session['row_184'] = request.POST.get('row184')
    request.session['row_185'] = request.POST.get('row185')
    request.session['row_186'] = request.POST.get('row186')
    request.session['row_187'] = request.POST.get('row187')
    request.session['row_188'] = request.POST.get('row188')
    request.session['row_189'] = request.POST.get('row189')
    request.session['row_190'] = request.POST.get('row190')
    request.session['row_191'] = request.POST.get('row191')
    request.session['row_192'] = request.POST.get('row192')
    return render(request, 'page8.html')


def page9(request):
    request.session['row_193'] = request.POST.get('row193')
    request.session['row_194'] = request.POST.get('row194')
    request.session['row_195'] = request.POST.get('row195')
    request.session['row_196'] = request.POST.get('row196')
    request.session['row_197'] = request.POST.get('row197')
    request.session['row_198'] = request.POST.get('row198')
    request.session['row_199'] = request.POST.get('row199')
    request.session['row_200'] = request.POST.get('row200')
    request.session['row_201'] = request.POST.get('row201')
    request.session['row_202'] = request.POST.get('row202')
    request.session['row_203'] = request.POST.get('row203')
    request.session['row_204'] = request.POST.get('row204')
    request.session['row_205'] = request.POST.get('row205')
    request.session['row_206'] = request.POST.get('row206')
    request.session['row_207'] = request.POST.get('row207')
    request.session['row_208'] = request.POST.get('row208')
    request.session['row_209'] = request.POST.get('row209')
    request.session['row_210'] = request.POST.get('row210')
    request.session['row_211'] = request.POST.get('row211')
    request.session['row_212'] = request.POST.get('row212')
    request.session['row_213'] = request.POST.get('row213')
    request.session['row_214'] = request.POST.get('row214')
    request.session['row_215'] = request.POST.get('row215')
    request.session['row_216'] = request.POST.get('row216')
    return render(request, 'page9.html')


def respostas_teste(request):
    request.session['row_217'] = request.POST.get('row217')
    request.session['row_218'] = request.POST.get('row218')
    request.session['row_219'] = request.POST.get('row219')
    request.session['row_220'] = request.POST.get('row220')
    request.session['row_221'] = request.POST.get('row221')
    request.session['row_222'] = request.POST.get('row222')
    request.session['row_223'] = request.POST.get('row223')
    request.session['row_224'] = request.POST.get('row224')
    request.session['row_225'] = request.POST.get('row225')
    request.session['row_226'] = request.POST.get('row226')
    request.session['row_227'] = request.POST.get('row227')
    request.session['row_228'] = request.POST.get('row228')
    request.session['row_229'] = request.POST.get('row229')
    request.session['row_230'] = request.POST.get('row230')
    request.session['row_231'] = request.POST.get('row231')
    request.session['row_232'] = request.POST.get('row232')
    request.session['row_233'] = request.POST.get('row233')
    request.session['row_234'] = request.POST.get('row234')
    request.session['row_235'] = request.POST.get('row235')
    request.session['row_236'] = request.POST.get('row236')
    request.session['row_237'] = request.POST.get('row237')
    request.session['row_238'] = request.POST.get('row238')
    request.session['row_239'] = request.POST.get('row239')
    request.session['row_240'] = request.POST.get('row240')
    write_pdf(TEMPLATE_PATH, OUTPUT_PATH, request.session)
    print(request.session)
    return render(request, 'respostas_teste.html')


def download_pdf_file(request):
    file_name = 'neo_resp.pdf'
    # Defina o caminho completo do arquivo
    path_file = DIR_BASE + '/static/files/' + file_name
    response = HttpResponse(open(path_file, 'rb').read())
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = "attachment; file_name =% s " % file_name
    return response
