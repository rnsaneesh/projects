import random
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from termcolor import colored
import win32com.client as mouth
import smtplib
import random
from IPython.display import Image
# voice assitant
speaker_number = 1
voice = mouth.Dispatch("SAPI.SpVoice")
vcs = voice.GetVoices()
vcs.Item (speaker_number) .GetAttribute ("Name")
voice.Voice
voice.SetVoice(vcs.Item(speaker_number))
voice.speak("Hello, I m your default voice assistant zero two ")
print(colored(("Hello, I m your default voice assistant zero two!"),'yellow'))
voice.Speak("Welcome to hotel intercontinental")
display(Image(r"C:\Users\acer\Desktop\ip project\welcome.jpg",width=800,height=0.2))
display(Image(r"C:\Users\acer\Desktop\ip project\header.jpg",width=500,height=20,))

#LOGIN PROCESS
voice.speak("enter your email id")
email_id=input(colored(('Enter your email id '),'red'))
content1=random.randint(100000,999999)
content=str(content1)
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('gmail','****')
mail.sendmail('gmail',email_id,content)
mail.close()
voice.Speak("Enter the O T P sent to your email id")
#VERIFYING EMAIL ID USING THE OTP SENT
otp=int(input(colored(('Enter the OTP sent to your email id '),'green')))
if otp==content1:
 voice.speak("your email is verified")
 print(colored(("Your email id is verified"),'blue'))
else:
 voice.speak("please check your email")
 print(colored(("please check your email"),'yellow'))
 
# Global List Declaration
name = []
phno = []
add = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
 
#GLOBAL VARIABLE DECLARATION
 
i = 0
 
# HOME FUNCTION
def Home():
  print(colored(("\t\t\t 1 ROOMS INFO\n"),'magenta'))
  print(colored(("\t\t\t 2 BOOKING\n"),'blue'))
  print(colored(("\t\t\t 3 ROOM SERVICE(MENU CARD)\n"),'green'))
  print(colored(("\t\t\t 4 AMENITIES\n"),'yellow'))
  print(colored(("\t\t\t 5 RECORD\n"),'red'))
  print(colored(("\t\t\t 0 EXIT\n"),'cyan'))
 
  ch=int(input("->"))
  if ch == 1:
    print(" ")
    Rooms_Info()

    
  elif ch == 2:
    print(" ")
    Booking()
  elif ch == 3:
    print(" ")
    restaurant()
  elif ch == 4:
    print(" ")
    amenities()
    
  elif ch == 5:
    print(" ")
    Record()
    
  else:
    exit()
# BOOKING FUNCTION
def Booking():
 
  # used global keyword to
  # use global variable 'i'
  global i
  print(" BOOKING ROOMS")

  print(" ")
  
  while 1:
    voice.speak("please enter your name")
    n = str(input(colored(("Name: "),'green')))
    voice.speak("please enter your phone number")
    p1 = str(input(colored(("Phone No.: "),'magenta')))
    voice.speak(" enter your address")
    a = str(input(colored(("Address: "),'red')))
  
  # CHECKS IF ANY FIELD IS N0T EMPTY 
  if n!="" and p1!="" and a!="":
    name.append(n)
    add.append(a)
    
  
  else:
    print("\tName, Phone no. & Address cannot be empty..!!")
  
  
  #SELECTING THE ROOM TYPE
  voice.speak("please select the room type")
  print(colored(("----SELECT ROOM TYPE----"),'magenta'))
  voice.speak("basic room")
  print(colored((" 1. BASIC ROOM "),'yellow'))
  display(Image(r"C:\Users\acer\Desktop\ip project\1 bed.jpg",width=350))
  voice.speak("modern room")

  print(colored((" 2. MODERN ROOM "),'green'))
  display(Image(r"C:\Users\acer\Desktop\ip project\2 bed suite.jpg",width=350))
  voice.speak("speacial suite")
  print(colored((" 3. SPECIAL SUITE"),'cyan'))
  display(Image(r"C:\Users\acer\Desktop\ip project\special suite.jpg",width=350))
  voice.speak("executive suite")
  print(colored((" 4. EXECUTIVE SUITE"),'red'))
  display(Image(r"C:\Users\acer\Desktop\ip project\executive.jpg",width=350))
  voice.speak("press 0 for room prices")
  print(("\t\tPress 0 for Room Prices"))
  
  ch=int(input("->"))
  
  # IF-CONDITONS TO DISPLAY ALLOTED ROOM
  
  if ch==0:
    print(colored((" 1. Basic Room - Rs. 3500"),'green'))
    print(colored((" 2. Modern Room - Rs. 4000"),'red'))
    print(colored((" 3. Special suite - Rs. 4500"),'blue'))
    print(colored((" 4. Executive suite - Rs. 5000"),'magenta'))
    ch=int(input("->"))

  if ch==1:
    room.append('Basic Room')
    print("Room Type- Basic Room") 
    price.append(3500)
    print("Price- 3500")
  elif ch==2:
    room.append('Modern Room')
    print("Room Type- Modern Room")
    price.append(4000)
    print("Price- 4000")
  elif ch==3:
    room.append('Special Suite')
    print("Room Type- Special suite")
    price.append(4500)
    print("Price- 4500")
  elif ch==4:
    room.append('Executive Suite')
    print("Room Type-Executive Suite ")
    price.append(5000)

    print("Price- 5000")
  else:
    print(" Wrong choice..!!")
  
  # randomly generating room no. and customer
  # id for customer
  rn = random.randrange(40)+300
  cid = random.randrange(40)+10
  
  
  # checks if alloted room no. & customer
  # id already not alloted
  while rn in roomno or cid in custid:
    rn = random.randrange(60)+300
    cid = random.randrange(60)+10
  
  rc.append(0)
  p.append(0)
  
  if p1 not in phno:
    phno.append(p1)
  elif p1 in phno:
    for n in range(0,i):
      if p1== phno[n]:
        if p[n]==1:
           phno.append(p1)

  elif p1 in phno:
    for n in range(0,i):
      if p1== phno[n]:
        if p[n]==0:
          print("\tPhone no. already exists and payment yet not done..!!")
  name.pop(i)
  add.pop(i)
  checkin.pop(i)
  checkout.pop(i)
  Booking()
  print("")
  print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
  print("Room No. - ",rn)
  print("Customer Id - ",cid)
  roomno.append(rn)
  custid.append(cid)
  i=i+1
  n=int(input("0-BACK\n ->"))
  if n==0:
    Home()
  else:
    exit()
  # ROOMS INFO
def Rooms_Info():
  print(colored((" ------ HOTEL ROOMS INFO ------"),'blue'))
  print("")

  print("---------------------------------------------------------------")
  print(colored(("BASIC ROOM"),'green'))
  print("---------------------------------------------------------------")
  print(colored(("Room amenities include: 1 Double Bed, Television, Telephone,"),'yellow'))
  print(colored(("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and"),'yellow'))
  print(colored(("an attached washroom with hot/cold water.\n"),'yellow'))
  print("---------------------------------------------------------------")
  print(colored(("MODERN ROOM"),'red'))
  print("---------------------------------------------------------------")
  print(colored(("Room amenities include: 1 Double Bed, Television, Telephone,"),'cyan'))
  print(colored(("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and"),'cyan'))
  print(colored(("an attached washroom with hot/cold water + centralized air conditioner.\n"),'cyan'))
  print("---------------------------------------------------------------")
  print(colored(("SPECIAL SUITE"),'magenta'))
  print("---------------------------------------------------------------")
  print(colored(("Room amenities include: 1 Double Bed + 1 Single Bed, Television,"),'green'))
  print(colored(("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1"),'green'))
  print(colored(("Side table, Balcony with an Accent table with 2 Chair and an"),'green'))

  print(colored(("attached washroom with hot/cold water + centralized air conditioner and complimentary breakfast.\n"),'green'))
  print("---------------------------------------------------------------")
  print(colored(("EXECUTIVE SUITE"),"grey"))
  print("---------------------------------------------------------------")
  print(colored(("Room amenities include: 1 Double Bed + 1 Single Bed, Television,"),'red'))
  print(colored(("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, "),'red'))
  print(colored(("1 Side table, Balcony with an Accent table with 2 Chair and an"),'red'))
  print(colored(("attached washroom with hot/cold water +centralized air conditioner and a complimentary candle light dinner.\n\n"),'red'))
  print("---------------------------------------------------------------")
  print()
  col=[9000,12000,9800,7300]
  type_of_room=['basic','modern','special','executive']
  plt.title("guests best choice")
  plt.axis("equal")
  plt.pie(col,labels=type_of_room,autopct="%5.2f%%")
  plt.show()
  n=int(input("0-BACK\n ->"))
  if n==0:
    Home()
  else:
    exit()

# RESTAURANT FUNCTION
def restaurant():
  voice.speak("please enter the customer id")
  ph=int(input("Customer Id: "))
  voice.speak("id verified")
  voice.speak("welcome to our virtual kitchen")
  voice.speak("we have special cuisine with delicious taste and luscious dishes")
  voice.speak("choose the number of the dishes")
  global i
  f=0
  r=0
  for n in range(0,i):
    if custid[n]==ph and p[n]==0:
      f=1
    print(pd.read_csv(r"C:\Users\acer\Desktop\ip project\INDIAN CUISINE.csv",index_col=[0]))
    print("Press 0 -to end ")
  ch=1
  while(ch!=0):

    ch=int(input(" -> "))

  # if-elif-conditions to assign item
  # prices listed in menu card
    if ch==1 or ch==31 or ch==32:
      rs=70
      r=r+rs
    elif ch<=4 and ch>=2:
      rs=100
      r=r+rs
    elif ch<=6 and ch>=5:
      rs=120
      r=r+rs
    elif ch<=8 and ch>=7:
      rs=100
      r=r+rs
    elif (ch<=10 and ch>=9) or ch==34:
      rs=80
      r=r+rs
    elif ch<=13 and ch>=11:
      rs=130
      r=r+rs
    elif ch<=18 and ch>=14:
      rs=120
      r=r+rs
    elif (ch<=23 and ch>=19) or ch==29:
      rs=150
      r=r+rs
    elif ch<=27 and ch>=24:
      rs=250
      r=r+rs
    elif ch==30 or ch==28:
      rs=230
      r=r+rs
    elif ch<=33 and ch>=31:
      rs=70
      r=r+rs
    elif ch<=37 and ch>35:
      rs=150
      r=r+rs
    elif ch<=39 and ch>=38:
      rs=160
      r=r+rs
    elif ch<=46 and ch>=40:
      rs=100
      r=r+rs
    elif ch==0:
      pass
    else:
      print("Wrong Choice..!!")
      print("Total Bill: ",r)
 
 # updates restaurant charges and then
 # appends in 'rc' list
  r=r+rc.pop(n)
  rc.append(r) 
  
    

  if f == 0:
    voice.speak("invalid customer id")
    print("Invalid Customer Id")
    n=int(input("0-BACK\n ->"))
  if n==0:
    Home()
  else:
    exit()
 
 
# AMENITIES FUNCTION 
def amenities():
  voice.speak("enter the customer id")
  ph=int(input("Customer Id: "))
  voice.speak("id verified")
  global i
  f=0
  for n in range(0,i):
    if custid[n]==ph and p[n]==0:
      f=1
  voice.speak("we have various amenities for our customers,please feel free to use it")
  print(colored(("AMENITIES:"),'cyan'))
  voice.speak("swimming pool")
  print(colored(("1,SWIMMING POOL"),'green'))
  display(Image(r"C:\Users\acer\Desktop\ip project\pool.jpg",width=500))

  voice.speak("gym")
  print(colored(("2,GYM"),'yellow'))
  display(Image(r"C:\Users\acer\Desktop\ip project\gym.jpg",width=500))
  voice.speak("spa")
  print(colored(("3,SPA"),'red'))
  display(Image(r"C:\Users\acer\Desktop\ip project\spa.jpg",width=500))
  voice.speak("please choose ur aminety")
  a=int(input("choose your aminety:"))
  time1 = {
  "1": "10.00am-11.00am",
  "2": "11.10am-12.10pm",
  "3": "12.20pm-1.20pm",
  "4": "2.30pm-3.30pm",
  "5": "3.40pm-4.40pm",
  "6": "10.00pm-11.00pm"
  }
  time2 = {
  "1": "6.00am-7.00am",
  "2": "7.00am-8.00am",
  "3": "8.00am-9.00am",
  "4": "9.00am-10.00am",
  "5": "7.30pm-8.30pm",
  "6": "8.30pm-9.30pm"

  }
  time3 = {
  "1": "2.00pm-2.30pm",
  "2": "5.00pm-5.300pm",
  "3": "5.30pm-6.00pm",
  "4": "6.00pm-6.30pm",
  "5": "6.30pm-7.00pm",
  "6": "7.00pm-7.30pm"
  }
  if a == 1:
    print(colored(("choose your time:"),'red'))
    voice.speak("these are the available time intervals")
    print(colored((time1),'cyan'))
    voice.speak("select your time")
    t = input("select your time:")
    x = time1[t]
    voice.speak("your selected time interval is"+x)
    print(colored(("thanks for cooperating!!your selected time interval: "+x),'magenta'))
  elif a == 2:
    print(colored(("choose your time:"),'red'))
    voice.speak("these are the available time intervals")
    print(colored((time2),'green'))
    voice.speak("select your time")

    t = input("select your time:")
    x = time2[t]
    voice.speak("your selected time interval is"+x)
    print(colored(("thanks for cooperating!!your selected time interval:"+x),'magenta'))
  elif a == 3:
    print(colored(("choose your time:"),'red'))
    voice.speak("these are the available time intervals")
    print(colored((time3),'yellow'))
    voice.speak("select your time")
    t = input("select your time:")
    x = time3[t]
    voice.speak("your selected time interval is"+x)
    print(colored(("thanks for cooperating!!your selected time interval:"+x),'magenta'))
  else:
    print("wrong choice")
    if f == 0:
      print("Invalid Customer Id")
      n = int(input("0-BACK\n ->"))
    if n == 0:
      Home()
    else:
      exit() 

# RECORD FUNCTION
def Record():
 
  xy=pd.DataFrame({'EMAIL_ID':email_id,'NAME':name,'PHONE_NO':phno})
  xy.to_csv(r"C:\Users\acer\Desktop\ip project\record.csv")
  # checks if any record exists or not
  if phno!=[]:
    print(" *** HOTEL RECORD ***\n")
    print("| NAME | PHONE NO. | ADDRESS | ROOM TYPE | PRICE |")
    print("----------------------------------------------------------------------------------------------------------------------")
  
    for n in range(0,i):
      print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",room[n],"\t|",price[n])
      print("----------------------------------------------------------------------------------------------------------------------")
  
  else:
    print("No Records Found")
    print("NOTE:A COPY OF RECORD IS SAVED BY MANAGEMENT FOR SECURITY PURPOSES") 
    n = int(input("0-BACK\n ->"))
    if n == 0:
      Home()
    else:
      exit()
  # Driver Code
Home()