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
        
        
def graficoLineas():
    

   
    Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
    Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    
    plt.plot(Year, Unemployment_Rate, color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Unemployment Rate', fontsize=14)
    plt.grid(True)
    plt.savefig("graficoLineas.png")
        
        


graficoLineas();
        
pdf = PDF('P', 'mm', 'Letter')



# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page

pdf.add_page()
pdf.image("graficoLineas.png");
# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

pdf.add_page()
# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)



for i in range(1, 41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=1)

pdf.output('pdf_2.pdf')