class myexeption(Exception):
    def __init__(self, err):
        print(f"Mira boludo lo que haces: {err}")
        
try:         
    raise myexeption("Jajajaja tonto")
except:
    print("Tonto sopilote de puta que haces pelotudo?")
    
    
raise myexeption("Jajajaja tonto")