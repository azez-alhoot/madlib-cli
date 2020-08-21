import re

def  read_template(file_path):
    lst = []
    with open(file_path,'r') as f :
        constant = f.read()
        res = re.findall(r'\{.*?\}', constant)
        for i in res:
            lst.append(i.strip("{ }"))
    return lst


def parse(file_path):
    with open(file_path,'r') as f :
        constant = f.read()
        res = re.sub(r'\{.*?\}' , '{}' , constant )
    return res


def merge(words,file_path):
    constant = parse(file_path)
    with open("assets/madlip_cli_copy.txt",'w') as f2:
        const2 = f2.write(constant.format(*words))
    with open("assets/madlip_cli_copy.txt",'r') as f3:
        const3 = f3.read()
    return const3


if __name__ == "__main__":
    print("""

    Put words as called for in the spaces and create a story by complete
    entring the values to create a story like Mad Libs it's fun. 
    What you've created may end up being fantastic, screamingly funny, shocking, silly, crazy 
    or just plain dumb. 
    It all depends upon the words you've chosen and how they "fit" into the Madlibs story!

    """)
    file_path = "assets/madlip_cli.txt"
    read_template(file_path)
    parse(file_path)
    ans = []
    lst = read_template(file_path)
    for i in lst:
        a = input(f'inter a {i}:')
        ans.append(a)
    print(merge(ans,file_path))