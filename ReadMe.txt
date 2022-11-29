**********************************
Generated-Bills.txt
----------------------------------
used to stored generated bills list


**********************************
For PDFs... FPDF library
----------------------------------
to install --- pip install fpdf

import --- from fpdf import FPDF

variable --- pdf = FPDF()

add page --- pdf.add_page()

setup --- pdf.set_font("Arial", size = 15)

heading --- pdf.cell(200, 10, txt = "GeeksforGeeks", ln = 1, align = 'C')

body --- pdf.cell(200, 10, txt = "A Computer Science portal for geeks.", ln = 2, align = 'C')

save --- pdf.output("GFG.pdf")