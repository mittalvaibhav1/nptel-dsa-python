def threesquares(m):
  if(m<0):
    return False
  else:
      i=0
      while(4**i<=m):
          for n in range(m//(4**i)):
              if(4**i)*(8*n+7)==m:
                  return False
          i=i+1 
      return True      
          
def repfree(s):
  for i in range(len(s)-1):
    if(s[i] in s[i+1:]):
      return False
  return True 

def hillvalley(l):
    if(len(l)==0):
      return False
    if(l[0]==max(l)):
        i=0
        while(i<len(l)-1 and l[i]>l[i+1]):
            i=i+1
        if(i==len(l)-1):
          return False
        while(i<len(l)-1):
            if(l[i]>l[i+1]):
                return False
            else:
                i=i+1
        return True
    else:
        i=0
        while(i<len(l)-1 and l[i]<l[i+1]):
            i=i+1
        if(i==len(l)-1):
          return False    
        while(i<len(l)-1):
            if(l[i]<l[i+1]):
                return False
            else:
                i=i+1
        return True