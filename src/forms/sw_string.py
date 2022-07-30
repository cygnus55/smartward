def isEmpty(*strings):
    for s in strings:
        s=s.strip()
        if (s==""):
            return True
        
def generateID(municipality,wardno,state):
    municipality=municipality.lower()
    try:
        index = municipality.rindex(" ")
        i = municipality[0:index]
        id = i.replace(" ", "")
        id = id
    except Exception:
        id = municipality.lower()
    return state+id+wardno

def generateList(**dic):
    string=[]
    for key,value in dic.items():
        string.append(key)
        string.append(value.replace("'",">>"))
    return string


