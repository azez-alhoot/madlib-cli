import re
print("""

Put words as called for in the spaces and create a story by complete
entring the values to create a story like Mad Libs it's fun. 
What you've created may end up being fantastic, screamingly funny, shocking, silly, crazy 
or just plain dumb. 
It all depends upon the words you've chosen and how they "fit" into the Madlibs story!

""")


lst = []
def  read_template():
    with open("assets/madlip_cli.txt",'r') as f :
        constant = f.read()
        res = re.findall(r'\{.*?\}', constant)
        for i in res:
            lst.append(i.strip("{ }"))

read_template()

def parse():
    with open("assets/madlip_cli.txt",'r') as f :
        constant = f.read()
        res = re.sub(r'\{.*?\}' , '{}' , constant )

        return res
parse()

ans = []
for i in lst:
    a = input(f'inter a {i}:')
    ans.append(a)

def merge():
    constant = parse()
    f2 =open("assets/madlip_cli_copy.txt",'+w')
    const2 = f2.write(constant.format(*ans))
    f2.close()
    return const2
merge()

f3 =open("assets/madlip_cli_copy.txt",'r')
const3 = f3.read()
f3.close()
print(const3)
