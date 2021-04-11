from app import application


from flask import send_file, abort, Response, render_template


# from xhtml2pdf import pisa
from fpdf import FPDF
import os
import io
import json



@application.route('/test3')
def test2():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_font('Tahoma', '', 'Tahoma.ttf', uni=True)
    pdf.set_font("Tahoma", size=12)
    with open(os.getcwd()+'\\static\\example_data\\one.json') as f: 
        json_file = json.load(f)
        for page in json_file:
            pdf.add_page()
            for elem in page:
                if elem['type'] == 1:
                    pdf.set_xy(elem['x'] * 0.2645833333, elem['y'] * 0.2645833333)
                    pdf.multi_cell(elem['width']* 0.2645833333, 5, txt=elem['text'], border=1)
                else:
                    pdf.rect(elem['x'] * 0.2645833333, elem['y'] * 0.2645833333, elem['width']* 0.2645833333, elem['height']* 0.2645833333, style = '')
    
    pdf.output("simple_demo.pdf")
    return Response(pdf.output(dest='S'),  status=201, mimetype='application/pdf')
    