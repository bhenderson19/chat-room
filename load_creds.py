import os
path = os.path.dirname(os.path.realpath(__file__))+"/creds.txt"

def load_creds():
    f = open(path)
    creds = []
    for line in f:
        creds.append(line.split("=")[1].replace(" ","").replace("\n",""))
    return creds