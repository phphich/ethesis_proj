from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

from django.conf import settings
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from easy_pdf.rendering import render_to_pdf_response
from reportlab.pdfgen import canvas
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# def doreporteasy(request):
#     reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/Lib/site-package/reportlab/fonts')
#     pdfmetrics.registerFont(TTFont('THSarabunNew', 'thsarabunnew-webfont.ttf'))
#     pdfmetrics.registerFont(TTFont('THSarabunNew-Bold', 'thsarabunnew_bold-webfont.ttf'))
#     pdfmetrics.registerFont(TTFont('THSarabunNew-Italic', 'thsarabunnew_italic-webfont.ttf'))
#     pdfmetrics.registerFont(TTFont('THSarabunNew-BoldItalic', 'thsarabunnew_bolditalic-webfont.ttf'))
#     pdfmetrics.registerFontFamily('THSarabunNew', normal='THSarabunNew',
#                                   bold='THSarabunNew-Bold', italic='THSarabunNew-Italic',
#                                   boldItalic='THSarabunNew-BoldItalic')
#
#     context=({})
#     return render_to_pdf_response(request,'report.html', context)
#
# def xsreport(request):
#     return HttpResponse()

from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
def xreport(request):
    pdfmetrics.registerFont(TTFont('THSarabunNew', 'thsarabunnew-webfont.ttf'))
    template = get_template('report.html')
    context = {"Name":"I am ReportLab"}
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)

