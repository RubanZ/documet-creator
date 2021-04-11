from fpdf import FPDF
import os
import base64,io
import math

from app import application

from flask import send_file, abort, Response, render_template
from flask import request



@application.route('/create-doc/preview', methods=['GET', 'POST'])
def doc_preview():
    if request.method == 'POST':
        try:
            json_file = request.get_json()
            return Response(doc_create(json_file),  status=201, mimetype='application/pdf')
        except:
            return 'Там было какое-то исключение и я его придерживаюсь'
    else:
        abort(418)



class PDF(FPDF):

    def load_resource(self, reason, filename):
        if reason == "image":
            if filename.startswith("http://") or filename.startswith("https://"):
                f = BytesIO(urlopen(filename).read())
            elif filename.startswith("data"):
                f = filename.split('base64,')[1]
                f = base64.b64decode(f)
                f = io.BytesIO(f)
            else:
                f = open(filename, "rb")
            return f
        else:
            self.error("Unknown resource loading reason \"%s\"" % reason)


def doc_create(document):
    pixel = 0.2645833333
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_font('Tahoma', '', 'fonts/Tahoma.ttf', uni=True)
    pdf.set_font("Tahoma", size=12)

    for page in document:
        pdf.add_page()
        for elem in page:
            if elem['type'] == 1:
                pdf.set_fill_color(elem['backgroundColor']['r'], elem['backgroundColor']['g'], elem['backgroundColor']['b'])
                pdf.rect(elem['x'] * pixel, elem['y'] * pixel, elem['width']* pixel, elem['height']* pixel, style = 'F')
                
                # pdf.cell(elem['width']* pixel, h = 12/2, txt = elem['text'], border = 1, ln = 1, fill = True)
                pdf.set_font("Tahoma", size=12)
                # print(pdf.get_string_width(elem['text']))
                # print(elem['width']* pixel)
                # print(math.ceil(pdf.get_string_width(elem['text'])/(elem['width']* pixel)))
                # print(elem['height']* pixel)
                # print((elem['height'] - math.ceil(pdf.get_string_width(elem['text'])/(elem['width']* pixel))*12*1.42857)*pixel)
                pdf.set_xy(elem['x'] * pixel, elem['y'] * pixel + (elem['height'] - math.ceil(pdf.get_string_width(elem['text'])/(elem['width']* pixel))*12*1.42857)*pixel/2)
                pdf.multi_cell(elem['width']* pixel, 12*1.42857*pixel, txt=elem['text'], fill=True, align='C')
                # pdf.cell(elem['width']* pixel, h = 0.8, txt = '', border = 1, ln = 1, fill = True)
            else:
                pdf.image(elem['img'], elem['x'] * pixel, elem['y'] * pixel, elem['width']* pixel, elem['height']* pixel)

    pdf.output("simple_demo.pdf")
    return pdf.output(dest='S')

