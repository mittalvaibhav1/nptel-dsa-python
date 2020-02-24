ListBooks=[]
ListUsers=[]
ListCheckouts=[]
ListFinal=[]
currInp=input();

while(True):
  currInp=input()
  if(currInp=="Borrowers"):
    break
  else:
    ListBooks.append(currInp)
    
while(True):
  currInp=input()
  if(currInp=="Checkouts"):
    break
  else:
    ListUsers.append(currInp)
    
while(True):
  currInp=input()
  if(currInp=="EndOfInput"):
    break
  else:
    ListCheckouts.append(currInp)    

for i in range(len(ListBooks)):
      Book=ListBooks[i].split("~")
      for j in range(len(ListCheckouts)):
        Check=ListCheckouts[j].split("~")
        if(Book[0]==Check[1]):
            for k in range(len(ListUsers)):
              User=ListUsers[k].split("~")
              if(User[0]==Check[0]):
                ListFinal.append(Check[2]+"~"+User[1]+"~"+Book[0]+"~"+Book[1])
ListFinal.sort()
for i in ListFinal:
  print(i)
  