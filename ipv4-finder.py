import socket
webname=input("Enter the name of website or simply paste url :")
while True :
    try :
       Ipaddress=socket.gethostbyname(webname)
       print(f"The ip-address of {webname} is {Ipaddress}")
    except socket.gaierror :
      print("The website doesn't exist !!!")
    break