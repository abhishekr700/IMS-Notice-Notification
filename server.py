# ===  SCRIPT BEGIN
#!/usr/bin/env python
# coding: utf-8

# In[93]:


import requests as r
import time
from bs4 import BeautifulSoup
import smtplib
from os import environ

# In[94]:


def notify(newd,origd):
    print("IMS NOTIFICATION PAGE CHANGED")
    print("Add:",newd)
    sendMail(newd,origd)


# In[95]:


def sendMail(newd,origd):
    # creates SMTP session 
    
    #port = int(environ.get('PORT', 587))
    #print(port)
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login("MoneyGust101@gmail.com", "MoneyGust@123") 

    # message to be sent
    msg = str("Subject:[BOT]IMS NOTIFICATION UPDATE \n\nNew:" + newd + "\n"+ "Old:" + origd)
    print(type(msg))
    #msg = "Message_you_need_to_send"
    #print(msg)
    #print(type(msg))
    
    # sending the mail 
    s.sendmail("MoneyGust101@gmail.com", "abhishekr700@gmail.com", msg)
    s.sendmail("MoneyGust101@gmail.com", "aakashgoryan@gmail.com", msg)

    # terminating the session 
    s.quit() 


# In[96]:


#url = "http://1ab61060.ngrok.io/Temp.html"
url = "https://www.imsnsit.org/imsnsit/notifications.php"
data = r.get(url)
plain = data.text
obj = BeautifulSoup(plain,"html.parser")
t = obj.find_all("tr")[3].find_all("td")[1].find_all("font")[0].text
origData = t
print("Original:",origData)


# In[97]:


changed = False
while  not changed:
    print("Loop Run ")
    time.sleep(300)
    #5 min delay
    print("Making Request")
    
    data = r.get(url)
    plain = data.text
    obj = BeautifulSoup(plain,"html.parser")
    newData = obj.find_all("tr")[3].find_all("td")[1].find_all("font")[0].text
    data.close()
    if newData != origData:
        notify(newData,origData)
        origData = newData





# === SCRIPT END
