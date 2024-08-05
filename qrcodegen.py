import qrcode
from PIL import Image
import validators
import requests

def main():
    qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=5,border=4,
                 ) #QRCODE class is selected from qrcode module which is basically used to change the view of qrcode like its size colour etc
    
    
    url=check()
    
    qr.add_data(url)#at first qr was used as alias but now qr is used as data since we put data i.e. link in it
    
    qr.make(fit=True)#if there's some value in add_data then only it will move forward
    img=qr.make_image(fill_color="red",back_color="white")
    #now we save using .save() fcn
    img.save("QR_Code.png")
def check():
    url=input("Please enter your link ")
    c=input("please press 'a' + |Enter| if you have input a url else just press |Enter| ").lower()

    if c=="a":
        if validators.url(url):#
            try:
                response=requests.get(url)
                if 200<=response.status_code<400:
                    print("xx url is working xx")
                    return url
            except requests.RequestException as e:
                print("Error 404")
        else:
            print("link isn't syntactically correct")
    else:
        return url
if __name__=="__main__":
    main()

    



            




    


