from fpdf import FPDF
import datetime
import os
import pyminizip

def gen_now_str_pdfs(n):
    pdfs=[]
    locations=[]
    for i in range(0,n):
        now_str = datetime.datetime.now().strftime("%H-%M-%S_%f")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(40, 10, now_str)
        out_pdf_name = "{}.pdf".format(now_str)
        pdf.output(out_pdf_name)
        pdfs.append(out_pdf_name)
        locations.append(".")
    return pdfs,locations

pdfs,locations =  gen_now_str_pdfs(2)

dest = "enc_{}.zip".format(pdfs[0].split(".")[0])
password = "SecreT"

pyminizip.compress_multiple(pdfs, locations, dest, password, 1)

for pdf in pdfs:
    os.remove(pdf)
