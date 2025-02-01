from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
import locale
import os
import platform

def imprimir(self):
    # Cabeçalho do Relatório
    today = date.today()
    d3 = today.strftime("%d/%m/%y")
        
    cnv = canvas.Canvas("vendas.pdf")
    width, height = A4
    print("Largura= ", width, "  Altura= ", height)
    cnv.setFont('Times-Roman', 14)
    cnv.setFillColorRGB(0, 0, 255)
    cnv.drawString(1, 820, "Sistema Comercial 1.0")
    cnv.setFont('Times-Bold', 14)
    cnv.setFillColorRGB(255, 0, 0)
    cnv.drawString(250, 820, "Pedido de Vendas")
    cnv.setFont('Times-Roman', 14)
    cnv.setFillColorRGB(0, 0, 255)
    cnv.drawString(540, 820, d3)
    # Cabeçalho do Pedido
    cnv.setLineWidth(2)
    cnv.line(0, 810, 595, 810)
    cnv.setFont('Times-Roman', 12)
    cnv.setFillColorRGB(0, 0, 0)
    cnv.drawString(10, 780, "Número do Pedido: " + self.txtnumvenda.get())
    cnv.drawString(200, 780, "Data do Pedido:   " + d3)
    
    cnv.drawString(10, 750, "Código do Cliente: " + self.txtcodcli.get())
    cnv.drawString(200, 750, "Nome do Cliente:  " + self.txtnomecli.get())
    cnv.setLineWidth(1)
    cnv.line(0, 720, 595, 720)
    # Linhas do Pedido
    cnv.setFont('Times-Bold', 12)
    cnv.drawString(1, 700, "Lin")
    cnv.drawString(40, 700, "Cod. Prod")
    cnv.drawString(130, 700, "Descrição")
    cnv.drawString(320, 700, "Quantidade")
    cnv.drawString(430, 700, "Valor Unitário")
    cnv.drawString(530, 700, "Valor")
    cnv.setFont('Times-Roman', 12)
    
    linha = 680
    for child in self.tree.get_children():
        print(self.tree.item(child)["values"])
        
        cnv.drawString(1, linha, str(self.tree.item(child)["values"][0]))
        cnv.drawString(40, linha, str(self.tree.item(child)["values"][1]))
        cnv.drawString(130, linha, self.tree.item(child)["values"][2])
        cnv.drawString(320, linha, str(self.tree.item(child)["values"][3]))
        cnv.drawString(430, linha, locale.currency(float(self.tree.item(child)["values"][4])))
        cnv.drawString(530, linha, locale.currency(float(self.tree.item(child)["values"][5])))
        linha = linha - 20
    # Total do Pedido
    cnv.line(0, linha, 595, linha)
    linha = linha - 20
    cnv.setFont('Times-Bold', 12)
    cnv.drawString(420, linha, "Total do Pedido ->")
    cnv.drawString(530, linha, locale.currency(float(self.txt_total.get().strip())))
    
    cnv.save()
    if platform.system() == "Windows":
        os.startfile("vendas.pdf")
    else:
        os.system("xdg-open vendas.pdf")