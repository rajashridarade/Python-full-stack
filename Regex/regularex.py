import  re

if __name__=="__main__":
    data = "firstbit soultion firstbit"
    patteren = re.compile(r"first")
    result = re.findall(patteren,data)
    print(result)