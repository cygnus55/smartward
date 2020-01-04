def isEmpty(*strings):
    for s in strings:
        if (s=="") or (s==" "):
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