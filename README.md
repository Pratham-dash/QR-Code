"# QR-Code" 
in this program we are making qr code for url or just plain text(according to user input)
for text we ask the user if its just plain test and to do that he has to press 'a' + enter
else he can just press anything or just enter 
to check if the url provided is correct we are using modules requests and validators: while requests get us the status code of the url {url is correct if ststus code is between 200 and 399 inclusive} and we use validators to check if the url is syntactically correct
then we just call the user input in main fcn and then generate the qr code and save it manually in QR_Code.png
