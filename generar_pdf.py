from fpdf import FPDF
import numpy as np
from matplotlib import pyplot as plt




class PDF(FPDF):
    
    
    
    def header(self):
        # Logo
        self.image('uq.png', 10, 8, 25)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Reporte', border=False, ln=1, align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')