def isEmpty(*strings):
    for s in strings:
        s=s.strip()
        if (s==""):
            return True
        
def generateID(state):
    import random
    pre=random.randint(11,51)
    post=random.randint(52,100)
    id="ward"+str(pre)+str(post)+'s'+str(state)
    return id

def generateList(**dic):
    string=[]
    for key,value in dic.items():
        string.append(key)
        string.append(value.replace("'",">>"))
    return string


