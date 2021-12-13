from fpdf import FPDF
import numpy as np
from matplotlib import pyplot as plt


class Grafica():
        
       

    def generarEstadisticaBarras():
        
        x = ["Ciencia","Comercio","Artes"]
        h = [200,300,500]
        c = ["red","green","orange"]
        plt.bar(x,h,width=0.5,color=c)
        plt.xlabel("Courses")
        plt.ylabel("Students enrolled")
        plt.title("")#Titulo de a grafica
        plt.savefig("graficobarras.png");        
            
            
    def generarEstadisticaPastel():
        plt.style.use("fivethirtyeight")

        slices = [59219, 55466, 47544, 36443, 35917]
        labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
        explode = [0, 0, 0, 0.1, 0]

        plt.pie(slices, labels=labels, explode=explode, shadow=True,
                    startangle=90, autopct='%1.1f%%',
                    wedgeprops={'edgecolor': 'black'})

        plt.title("My Awesome Pie Chart")
        plt.tight_layout()
        plt.savefig("graficoPastel.png");





