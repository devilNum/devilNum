import os,zipfile,base64
def com(filef, fileo):
    with open(filef, 'r') as fio:
        hil = fio.read()
    ft = ''
    comi = False
    i = 0
    while i < len(hil):
        if hil[i:i+2] == '/*':
            comi = True
            i += 2
            continue
        elif hil[i:i+2] == '*/':
            comi = False
            i += 2
            continue
        if not comi:
            ft += hil[i]
        i += 1
    with open(fileo, 'w') as fo:
        fo.write(ft)
Name = input('FILE: ')
Nam = input("Saved Encrypted: ")
zip_path = ".DEMO"
with open(f'{Name}','r') as l:
    V = l.read()
with open(f'{Nam}','w') as k:
    k.write(f'''import os
d = input("اضغط Enter للخروج او اكتب اي شيئ للاستمرار: ")
if d == "":
    os._exit(0)
{V}\n''')
Names = Nam.replace('.py','')
os.system(f'cython --embed -3 {Nam} -o {Names}.c')
Names = Nam.replace('.py','')
com(f'{Names}.c',f'{Names}.c')
with open(f'{Names}.c','r') as g:
    co = g.read()
a=f'''import os
import sys
PREFIX=sys.prefix
ExcuF = ".DEMO/{Names}"
MyHome ="export PYTHONHOME="+sys.prefix
Execu ="export PYTHON_EXECUTABLE="+ sys.executable
RUN = "./"+ ExcuF
if os.path.isfile(ExcuF):
    os.system(MyHome +"&&"+ Execu +"&&"+ RUN)
    exit(0)
C_SOURCE =r"""{co}"""
'''
b=f'''
C_FILE ="{Names}.c"
Vers = ".".join(sys.version.split(" ")[0].split(".")[:-1])
ElfF = ("gcc -I" + PREFIX + "/include/python" + Vers +" -o " + ExcuF + " " + C_FILE +" -L" + PREFIX + "/lib -lpython" + Vers)
with open(C_FILE, "w") as f:
    f.write(C_SOURCE)
os.makedirs(os.path.dirname(ExcuF),exist_ok=True)
os.system(MyHome +"&&"+ Execu +"&&" + ElfF +"&&"+ RUN)
os.remove(C_FILE)'''
with open(f'{Names}.c','r') as g:
    co = g.read()
    enc=a+b
with open(f'{Nam}.py','w') as k:
    k.write(enc)
os.system(f'python {Nam}.py')
Ff = '''E=print
B=''
A=chr
import zipfile as I,os as C,shutil as K,tempfile as L,sys as D,platform as M
def F():
    N=C.path.dirname(C.path.abspath(D.argv[0]));G=L.mkdtemp()
    try:
        O=C.path.abspath(D.argv[0])
        with I.ZipFile(O,'r')as P:P.extractall(G)
        F=M.machine();J={(lambda s:B.join(A(B^151)for B in s))([246,229,250,225,160,251]):(lambda s:B.join(A(B^11)for B in s))([106,121,102,110,106,105,98,38,125,60,106]),(lambda s:B.join(A(B^69)for B in s))([36,55,40,51,125,41]):(lambda s:B.join(A(B^179)for B in s))([210,193,222,214,210,209,218,158,197,132,210]),(lambda s:B.join(A(B^134)for B in s))([231,244,235]):(lambda s:B.join(A(B^177)for B in s))([208,195,220,212,208,211,216,156,199,134,208]),(lambda s:B.join(A(B^54)for B in s))([87,87,68,85,94,0,2]):(lambda s:B.join(A(B^4)for B in s))([101,118,105,50,48,41,114,60,101]),(lambda s:B.join(A(B^130)for B in s))([227,240,239,180,182]):(lambda s:B.join(A(B^199)for B in s))([166,181,170,241,243,234,177,255,166]),(lambda s:B.join(A(B^189)for B in s))([197,133,139]):(lambda s:B.join(A(B^200)for B in s))([176,240,254]),(lambda s:B.join(A(B^108)for B in s))([5,90,84,90]):(lambda s:B.join(A(B^39)for B in s))([95,31,17]),(lambda s:B.join(A(B^173)for B in s))([213,149,155,242,155,153]):(lambda s:B.join(A(B^71)for B in s))([63,127,113,24,113,115]),(lambda s:B.join(A(B^208)for B in s))([177,189,180,230,228]):(lambda s:B.join(A(B^176)for B in s))([200,136,134,239,134,132])}
        if F not in J:E((lambda s:B.join(A(B^171)for B in s))([254,197,216,222,219,219,196,217,223,206,207,139,202,217,200,195,194,223,206,200,223,222,217,206,145,139,142,216])%F);D.exit(1)
        Q=J[F];H=C.path.join(G,Q)
        if not C.path.exists(H):E((lambda s:B.join(A(B^97)for B in s))([52,15,18,20,17,17,14,19,21,4,5,65,0,19,2,9,8,21,4,2,21,20,19,4,91,65,68,18])%F);D.exit(1)
        C.chmod(H,493);C.chdir(N);R=(lambda s:B.join(A(B^128)for B in s))([229,248,240,239,242,244,160,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,189,164,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,186,165,243,175,236,233,226,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,200,207,205,197,189,165,243,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,223,197,216,197,195,213,212,193,194,204,197,189,165,243,160,166,166,160,165,243,160,165,243])%(D.prefix,D.prefix,D.executable,H,' '.join(D.argv[1:]));C.system(R)
    except I.BadZipFile:E((lambda s:B.join(A(B^206)for B in s))([139,188,188,161,188,244,238,154,166,171,238,180,167,190,238,168,167,162,171,238,167,189,238,173,161,188,188,187,190,186,171,170,238,161,188,238,160,161,186,238,175,238,180,167,190,238,168,167,162,171,224]))
    except Exception as S:E((lambda s:B.join(A(B^195)for B in s))([130,173,227,166,177,177,172,177,227,172,160,160,182,177,177,166,167,249,227,230,176])%S)
    finally:K.rmtree(G)
if __name__==(lambda s:B.join(A(B^30)for B in s))([65,65,115,127,119,112,65,65]):F()'''
with open(f'.DEMO/{Names}','rb') as j:
    D = j.read()
def create_zip_with_so_files_and_main(zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr('__main__.py', Ff)
        zipf.writestr('arm64-v8a', D)
        create_zip_with_so_files_and_main(zip_path)
with open('.DEMO', 'rb') as F:
    om = F.read()
kl = base64.b64encode(om).decode()
oip = f'''import os as D, sys as S
from base64 import b64decode as N 
G, C = '.DEMO', {kl!r}  
try:  
    open(G, 'wb').write(N(C))  
    D.system(f'python3 {{G}} {{" ".join(S.argv[1:])}}')  
finally:  
    print(G) if D.path.exists(G) else 0'''
with open(f'{Name}_demo.py', 'w') as p:
    p.write(oip)