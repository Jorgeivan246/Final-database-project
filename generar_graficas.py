from fpdf import FPDF
import numpy as np
from matplotlib import pyplot as plt
from generar_pdf import PDF

class Grafica():
        
    def __init__(self):
        self.count=0

    def generarEstadisticaBarrasRecepcion(self,datos):
        
        
        x = ["Recepcion1","Recepcion2","Recepcion3","Recepcion4"]
        h = [datos[0] ,datos[1],datos[2],datos[3]]
        c = ["red","green","orange","blue"]
        plt.bar(x,h,width=0.5,color=c) 
        plt.xlabel("Recepciones")   
        plt.ylabel("Cantidad")   
        plt.title("Recepciones ")
        plt.savefig("graficoBarrasRecepcion.png");
        
        
    
    def generarEstadisticaBarrasEnvasado(self,datos2):
        
        
        x = ["Cuñete","Pinpina","Tambor de acero ","Tambor de plastico"]
        h = [datos2[0] ,datos2[1],datos2[2],datos2[3]]
        c = ["red","green","orange","blue"]
        plt.bar(x,h,width=0.5,color=c) 
        plt.xlabel("Tipo de envasado")   
        plt.ylabel("Peso total")   
        plt.title("Peso bruto ")
        plt.savefig("graficoBarrasEnvasado.png");
            
            
    def generarEstadisticaBarrasPastel(self,datos2):
        plt.style.use("fivethirtyeight")

        slices = [datos2[0] ,datos2[1],datos2[2],datos2[3]]
        labels = ['Cuñete', 'Pinpina', 'Tambor de acero', 'Tambor de plastico']
        explode = [0, 0, 0.1, 0]

        plt.pie(slices, labels=labels, explode=explode, shadow=True,
                    startangle=90, autopct='%1.1f%%',
                    wedgeprops={'edgecolor': 'black'})

        plt.title("Tipo de envasado")
        plt.tight_layout()
        plt.savefig("graficoPastelEnvasado.png");
        
        
    def graficoLineas(self):
   
        Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
        Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        
        plt.plot(Year, Unemployment_Rate, color='red', marker='o')
        plt.title('Unemployment Rate Vs Year', fontsize=14)
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Unemployment Rate', fontsize=14)
        plt.grid(True)
        plt.savefig("graficoLineas.png")
        
    def generarPDf(self,nombreImagen):
        pdf = PDF('P', 'mm', 'Letter')


        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto = True, margin = 15)

        #Add Page

        pdf.add_page()
        pdf.image(nombreImagen+".png");
        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)

        pdf.add_page()
        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)

        pdf.output('reporte'+  nombreImagen+'.pdf')
        
    