import threading
import requests
url="http://192.168.1.1"
while True :
 def uptask():
     response1=requests.post(url)
     print(response1.status_code)
    
 def downtask():
     response2=requests.post(url)
     print(response2.status_code)
    
 thread1=threading.Thread(target=uptask)
 thread2=threading.Thread(target=downtask)
 thread1.start()
 thread2.start()
 thread1.join()
 thread2.join()
