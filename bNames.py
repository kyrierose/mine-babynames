from bs4 import BeautifulSoup
import requests as r

def getNames():
    html = r.get("http://www.babynamewizard.com/the-top-1000-baby-names-of-2015-united-states-of-america")
    ht = html.text
    soup = BeautifulSoup(ht,'html.parser')
    i = 0
    for x in soup.find_all("td"):
        i+=1
        if i%4 == 2:
            print(x.get_text ())
        else:
            continue


def getLastName():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in alpha:
        print("Gathering "+ char)
        html = r.get("http://www.surnamedb.com/Surname?alpha="+char)
        html = html.text
        soup = BeautifulSoup(html,'html.parser')
        var = ['Col1','Col2','Col3']
        for col in var:
            str = ""
            for x in soup.find_all("div" , id = col):
                str += (x.get_text())

            with open("LastName.txt",'a') as f:
                f.write(str)

#Intiates from here.
getLastName()