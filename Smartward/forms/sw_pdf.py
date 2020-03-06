import pickle
from fpdf import FPDF

ward=open("ward.pickle",'rb')
wardinfo=pickle.load(ward)
municipality,address=wardinfo['municipality'],wardinfo['address']

logo="logo.png"

class Certificate():
    def __init__(self):
        #self.logopath=logopath
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addHeader()
        #self.pdf.output(pdffilepath)

    def addLogo(self,imgpath):
        self.pdf.image(imgpath,15,30,25,24.67)

    def addHeader(self):
        self.addLogo(logo)
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Schedule-12/13/14/15", ln=1, align='C')
        self.pdf.cell(180, 8, txt="(Related with Rule 7)", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Government of Nepal", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Ministry of Federal Affairs and Local Development", ln=1, align='C')
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180,8,txt="Office Of Local Registrar",ln=1,align='C')
        self.setOfficeAddress(municipality,address)

    def setOfficeAddress(self, municipality, address):
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180,8,txt=municipality,ln=1,align='C')
        self.pdf.cell(180,8,txt=address,ln=1,align="C")



class BirthCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Birth Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('birthcertificate.txt')
        #self.setBody('fdsf')

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def setBody(self,args):
        #print(args)
        contents=self.getfromtxt('birthcertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')

    def output(self):
        self.pdf.output("birthcertificate.pdf")

#a=BirthCertificate()
#a.setOfficeAddress('Namobuddha Municipality','Kavre')
#a.setBody(123)
#a.output("test.pdf")
