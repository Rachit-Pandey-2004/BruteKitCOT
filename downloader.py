import requests
from time import sleep
import os
_session=requests.Session()


from bs4 import BeautifulSoup


def download_img(endpoint:str,id:str):
    
    res=_session.get(endpoint)
    with open(f"{id}{endpoint.replace("http://10.1.1.5","")}","wb")as fs:
        fs.write(res.content)
        fs.close()

def img_parser(cont,id:str):
    soup = BeautifulSoup(cont.content, "html.parser")
    thumbnail_elements = soup.find_all("img")

    #print(thumbnail_elements)
    index=0
    for element in thumbnail_elements:
        if(index==0):
            os.mkdir(id)
            os.mkdir(f"{id}/student_image")
            os.mkdir(f"{id}/studentID_image")
            
            with open('%s/%s.html'%(id,id),'w')as fs:
                fs.write(cont.text)
                fs.close()
            index=1
        img=(element['src'].replace("..","http://10.1.1.5"))
        download_img(img,id)

def regis_form(id:str):
    endpoint="http://10.1.1.5/form/form.php?user_id=%s"%id
    try:
        data=_session.get(endpoint)
        img_parser(data,id)
    except:
        print("need cooldown for ID %s"%id)  
        sleep(3)
        data=_session.get(endpoint)
        img_parser(data,id)
    
    
def run(id):
    try: 
        print(f"searching {id}")
        regis_form(f"{id}")
        #sleep(1)
        pass
    except:
        print("reconnecting....")
        pass

print("enter range:\nx ->")
start=int(input())
print("\nend ->")
end=int(input())
for x in range(start,end):

    run(x)