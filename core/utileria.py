# Utilleria para renderizar pdf con template django
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_pdf(url_template, contexto={}):
    """
    renderiza un template django a documento PDF
    """
    template = get_template(url_template)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
        return None
