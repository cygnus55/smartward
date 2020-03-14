def isEmpty(*strings):
    for s in strings:
        s=s.strip()
        if (s==""):
            return True
        
def generateID(municipality,wardno,state):
    '''
    municipality=municipality.lower()
    try:
        index = municipality.rindex(" ")
        i = municipality[0:index]
        id = i.replace(" ", "")
        id = id
    except Exception:
        id = municipality.lower()
    return state+id+wardno
    '''
    import random
    pre=random.randint(11,51)
    post=random.randint(11,51)
    id=int(str(wardno)+str(pre)+str(state)+str(post))
    return id

def generateList(**dic):
    string=[]
    for key,value in dic.items():
        string.append(key)
        string.append(value.replace("'",">>"))
    return string

