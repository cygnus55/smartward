import pickle
from fpdf import FPDF
import nepali_date

today=nepali_date.NepaliDate.today()
today_date=str(today)[3:]

ward=open("ward.pickle",'rb')
wardinfo=pickle.load(ward)
municipality,address=wardinfo['municipality'],wardinfo['address']
wardno,state=wardinfo['wardno'],wardinfo['state']
email,mun_logo=wardinfo['email'] ,wardinfo['mun_logo']
phone,registrar_name=wardinfo['phone'],wardinfo['registrar_name']


logo="logo.png"
class Certificate():
    def __init__(self):
        #self.logopath=logopath
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addHeader()
        #self.pdf.output(pdffilepath)

    def addLogo(self):
        self.pdf.image(logo,15,30,25,24.67)

    def addHeader(self):
        self.addLogo()
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Schedule-12/13/14/15/16", ln=1, align='C')
        self.pdf.cell(180, 8, txt="(Related with Rule 7)", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Government of Nepal", ln=1, align='C')
        self.pdf.cell(180, 8, txt="Ministry of Federal Affairs and Local Development", ln=1, align='C')
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180,8,txt="Office Of Local Registrar",ln=1,align='C')
        self.setOfficeAddress(municipality,address)

    def addFooter(self):
        self.pdf.set_font("Times",'B',size=10)
        self.pdf.cell(180, 8, txt="Local Registrar's:", ln=1, align='L')
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180, 8, txt="Signature:", ln=1, align='L')
        self.pdf.cell(180, 8, txt="Name and Surname: "+registrar_name, ln=1, align='L')
        self.pdf.cell(180,8,txt="Date: "+today_date,ln=1,align='L')

    def setOfficeAddress(self, municipality, address):
        self.pdf.set_font("Times",size=10)
        self.pdf.cell(180,8,txt=municipality,ln=1,align='C')
        self.pdf.cell(180,8,txt=address,ln=1,align="C")
       
	def output(self):
        self.pdf.output("output/certificate.pdf")       



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
        print(args)
        contents=self.getfromtxt('txtfiles/birthcertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()


class MarriageCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Marriage Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('Marriagecertificate.txt')
        #self.setBody('fdsf')

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def setBody(self,args):
        print(args)
        contents=self.getfromtxt('txtfiles/marriagecertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class DeathCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Death Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('Marriagecertificate.txt')
        #self.setBody('fdsf')

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def setBody(self,args):
        print(args)
        contents=self.getfromtxt('txtfiles/deathcertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

        
class DivorceCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Divorce Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('Marriagecertificate.txt')
        #self.setBody('fdsf')

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def setBody(self,args):
        print(args)
        contents=self.getfromtxt('txtfiles/divorcecertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')
        self.addFooter()

class MigrationCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.pdf.set_font("Times",'BU',20)
        self.pdf.cell(180,8,txt='Migration Registration Certificate',ln=1,align='C')
        #self.setBody('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #self.getfromtxt('Marriagecertificate.txt')
        #self.setBody('fdsf')

    def getfromtxt(self,txt):
        content=''
        text=open(txt,'r')
        txt=text.readlines()
        return txt

    def setBody(self,args):
        print(args)
        contents=self.getfromtxt('migrationcertificate.txt')
        #args=('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        #contents=content.format('12321','2056/09/03','4233','Ram Hari Khatiwada','Hari Krishna Ghimere','Tilak Ghimere','Sunita Ghimere','Ghana Shyam Ghimere','05','Namobuddha','2056/01/03','1997/05/09','Methinkot Hospital','2023/05/06','Kavre','23452','2030/06/09','Kavre','875683')
        lines=[]
        for content in contents:
            lines.append(content.format(*args))
        for line in lines:
            self.pdf.set_font('Times',size=10)
            self.pdf.cell(1950,8,txt=line,ln=1,align='L')

    def setTable(self,data):
        col_width = self.pdf.w / 7.5
        row_height = self.pdf.font_size
        for row in data:
            for item in row:
                self.pdf.cell(col_width, row_height * 1,txt=item, border=1)
            self.pdf.ln(row_height * 1)
        self.addFooter()


class Recommendation():
    def __init__(self):
        self.pdf=FPDF()
        self.pdf.add_page()
        self.addHeader()
        self.addFooter()
        
   	def output(self):
        self.pdf.output("output/recommendationletter.pdf")

    def addLogo(self):
        self.pdf.image(logo, 5, 5, 12.5*1.5, (24.67*1.5)/2)
        try:
            self.pdf.image(mun_logo,185,5,18.75,18.5625)
        except Exception:
            pass

    def addHeader(self):
        self.addLogo()
        self.pdf.set_text_color(255,0,0)
        self.pdf.set_font("Times", size=18)
        self.pdf.cell(180, 6, txt=municipality.title()+" Municipality", ln=1, align='C',)
        self.pdf.set_font("Times", size=14)
        self.pdf.cell(180, 6, txt="Ward No. "+wardno+" Office", ln=1, align='C')
        self.pdf.set_font("Times", size=10)
        self.pdf.cell(180, 6, txt=address, ln=1, align='C')
        self.pdf.cell(180, 6, txt="State No. "+state+", Nepal", ln=1, align='C')
        self.pdf.cell(30,6,txt="Letter No.:",align='L')
        self.pdf.set_x(175)
        self.pdf.cell(30, 6, txt="Date: "+today_date,ln=1,align='L')
        self.pdf.cell(30, 6, txt="Invoice No.:", ln=1, align='L')

        y=self.pdf.get_y()
        self.pdf.set_draw_color(255,0,0)
        self.pdf.set_fill_color(255,0,0)
        self.pdf.rect(0,y+2,220,.75,'DF')

    def addFooter(self):
        self.pdf.set_y(-28)
        self.pdf.set_text_color(255, 0, 0)
        self.pdf.set_font('Times', '', 8)
        self.pdf.cell(0, 5,"Email: "+email+", Phone No.: "+phone, ln=1, align='C')
