import os
import requests
import socket

def ekraniTemizle():
    os.system("clear")

def ana_program():
    print("Web Scanner V1")
    print("Programmer: 0silat0r")
    print("Dipnot: Programin yasadisi faaliyetlerde kullanilmasi, kullanicinin insiyatifinde olan bir durumdur.\nBu programi yazan programcinin ortaya cikacak zararlardan sorumlu degildir.")
    
    hedef = input("Lutfen bir web adresi girin: ")
    r = requests.get(hedef)
    if r.status_code == 200:
        headers = r.headers
        content = r.text
        encoding = r.encoding
        hedef_host = hedef[8:]
        
        ipaddr = socket.gethostbyname(hedef_host)
        
        ekraniTemizle()
        print("HTTP 200 OK")
        print(f"Hedef Internet Adresi: {hedef}")
        print(f"Hedef Host: {hedef_host}")
        print(f"IP Adresi: {ipaddr}")
        print(f"HTTP Headers\n{headers}\n")
        print(f"Encoding: {encoding}\n")
        print(f"Content:\n{content}")
    else:
        print("Bir hata var. Lutfen daha sonra tekrar deneyin veya hedef degistirin.")

try:
    ekraniTemizle()
    ana_program()
except KeyboardInterrupt:
    print("\nProgramdan cikis yaptiniz!")
