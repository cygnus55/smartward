from fpdf import FPDF

logo="logo.png"

class PDF():
    def __init__(self):
        #self.logopath=logopath
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addLogo(logo)
        self.addHeader()
        #self.pdf.output(pdffilepath)

    def addLogo(self,imgpath):
        self.pdf.image(imgpath,15,30,25,24.67)

    def addHeader(self):
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Schedule-12/13/14/15", ln=1, align='C')
        self.pdf.cell(180, 8, txt="(Related with Rule 7)", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Government of Nepal", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Ministry of Federal Affairs and Local Development", ln=1, align='C')
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180,8,txt="Office Of Local Registrar",ln=1,align='C')

    def setOfficeAddress(self, municipality, district):
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180,8,txt=municipality,ln=1,align='C')
        self.pdf.cell(180,8,txt=district,ln=1,align="C")



class BirthCertificate(PDF):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',10)
        self.pdf.cell(180,8,txt='Birth Certificate',ln=1,align='C')

    def output(self,pdffilepath):
        self.pdf.output(pdffilepath)

a=BirthCertificate()
a.setOfficeAddress('Namobuddha Municipality','Kavre')
a.output("test.pdf")