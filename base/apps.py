from django.apps import AppConfig
import pdfrw



class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_pdf(input_pdf, output_pdf, data_dict):
    template_pdf = pdfrw.PdfReader('NEO1_form.pdf')

    annotations = template_pdf.pages[0][ANNOT_KEY]

    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    update = {
                        'V': data_dict[key],
                    }
                    annotation.update(pdfrw.PdfDict(**update))
        annotation.update(pdfrw.PdfDict(Ff=1))

    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write('NEO1_edit.pdf', template_pdf)
