import re

if __name__ == "__main__":
    data = '''101,Ram Nikam,24,Pune
            102,Radha Kadam,25,Nagpur'''
    pattern = re.compile(r"[A-Z][a-z]+\s[A-Z][a-z]+")
    result = re.finditer(pattern, data)
    print(result)
    for p in result:
        print(p)
