import ezgmail

class SWGmail():
    def __init__(self):
        ezgmail.init()
        self.mygmail=ezgmail.EMAIL_ADDRESS

    def sendRegistrationSuccessfulMail(self,login_id,municipality,wardno,state,address,phone,email_id,ip_address,password):
        sub="Welcome to SmartWard Family!"
        salutation="Congratulations!\nYour ward office has been sucessfully registered to Smartवडा.\n"
        info1="Here are your registration details:\n"+municipality+" Ward No. "+wardno
        info2="\nAddress: "+address+"\nState No. "+state
        info3="\nPhone: "+phone+"\nEmail: "+email_id
        ip="\nYou are logged in with system.\n\t\tIP Address: "+ip_address+"\nYour login credentials are:\n"
        login_credentials="Login ID: "+login_id+"\nLogin Gmail: "+email_id+"\nLogin Password: "+password
        ignore="\nIf you havenot applied for registration,please ignore this mail."
        end="\nThanks,\nSmartवडा Family"
        body=salutation+info1+info2+info3+ip+login_credentials+ignore+end
        ezgmail.send(email_id,sub,body)
        print("mail send")

    def sendLoginMail(self,email_id,ip):
        sub="New Login"
        info1="Your account has recently been logged in sucessfully in system with \n "
        info2="IP Address: "+ip
        info3="\nIf this wasn't you,try changing password immediately."
        info4="\nIgnore this mail if that was you, but caution is necessary for security."
        end="\nThanks,Smartवडा Family"
        body=info1+info2+info3+info4+end
        ezgmail.send(email_id,sub,body)

    def sendForgetPasswordMail(self,id,email,pswd):
        sub="Forget Password"
        info1="Following are your login credentials:"
        login_credentials = "\nLogin ID: " + id + "\nLogin Gmail: " + email + "\nLogin Password: " + pswd
        end = "\nThanks,Smartवडा Family"
        body=info1+login_credentials+end
        ezgmail.send(email,sub,body)