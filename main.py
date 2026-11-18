import os,json
from urllib.request import*
def P(p,b):return json.loads(urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode()).read())
ND=(-21,-19,-12,-8,8,12,19,21);BD=(-11,-9,9,11);RD=(-10,-1,1,10);AD=BD+RD
D2=dict(N=ND,B=BD,R=RD,Q=AD,K=AD)
VM=[0,100,320,330,500,950,1e5]
TN={c:i+1 for i,c in enumerate("PNBRQK")}
def TB(t):
 h=[(ord(c)-48-39*(c>"9")-13)*4 for c in t]
 return[h[(j//8)*4+min(j%8,7-j%8)]for j in range(64)]
PM=[None,TB("ddddeffbecbddddieefjffilppppdddd"),TB("135538de5efh5dhi5ehi5dfh38dd1355"),[0]*64,[0]*64,[0]*64,TB("ilfdilfdb88885535331533153315151")]
T={};N=0;NB=6e4;BM=[None]
TO=Exception
def F(fen):
 p=fen.split()
 b=" "*20+"".join(" "+"".join("."*int(ch)if ch<"9"else ch for ch in row)+" "for row in p[0].split("/"))+" "*20
 return(b,(1,-1)[p[1]=="b"],p[2].strip("-"),0 if p[3]=="-"else(70 if p[3][1]=="3"else 40)+ord(p[3][0])-96)
def G(st,cap):
 b,s,c,e=st;ms=[];ap=ms.append
 for i in range(21,99):
  x=b[i]
  if x=="."or x.isupper()!=(s>0):continue
  u=x.upper()
  if u=="P":
   d=-10*s;j=i+d
   def ap2(j):
    ap((i,j,"q"if j//10 in(2,9)else""))
   if b[j]==".":
    if j//10 in(2,9)or not cap:ap2(j)
    if not cap and i//10==(8 if s>0 else 3)and b[i+2*d]==".":ap((i,i+2*d,""))
   for dd in(d-1,d+1):
    j=i+dd;t=b[j]
    if(t not in" ."and t.isupper()!=(s>0))or j==e:ap2(j)
  elif u in D2:
   ds=D2[u];sl=u in"BRQ"
   for d in ds:
    j=i
    while 1:
     j+=d;t=b[j]
     if t==" "or(t!="."and t.isupper()==(s>0)):break
     if t!=".":
      ap((i,j,""));break
     if not cap:ap((i,j,""))
     if not sl:break
   if u=="K"and not cap and abs(i-60)==35:
    if("K"if s>0 else"k")in c and b[i+1:i+3]=="..":ap((i,i+2,""))
    if("Q"if s>0 else"q")in c and b[i-3:i]=="...":ap((i,i-2,""))
 return ms
def M(st,m):
 b,s,c,e=st;i,j,pr=m;x=b[i];L=list(b)
 L[i]=".";L[j]=(pr.upper()if s>0 else pr)if pr else x
 if x.upper()=="P"and j==e and b[j]==".":L[j+10*s]="."
 if x.upper()=="K"and abs(j-i)==2:
  r=(3,1)if j>i else(-4,-1);L[i+r[1]]=L[i+r[0]];L[i+r[0]]="."
 n=c
 for ch in("KQ"if x=="K"else"kq"if x=="k"else""):n=n.replace(ch,"")
 for q,ch in zip((91,98,21,28),"QKqk"):
  if i==q or j==q:n=n.replace(ch,"")
 return("".join(L),-s,n,(i+j)//2 if x.upper()=="P"and abs(j-i)==20 else 0)
def A(b,q,s):return any(m[1]==q for m in G((b,s,"",0),1))
def E(st):
 b=st[0];v=0
 for i in range(21,99):
  x=b[i]
  if x in". ":continue
  t=TN[x.upper()];y=(9-i//10)*8+i%10-1
  v+=(VM[t]+PM[t][y if x.isupper()else y^56])*(1 if x.isupper()else-1)
 return v
def O(st,ms,tt):
 b=st[0];sc=[]
 for m in ms:
  i,j,pr=m;v=0
  if m==tt:v=9e6
  elif b[j]!="."or pr:
   w=TN[b[j].upper()]if b[j]!="."else 1
   v=8e6+VM[w]*32-TN[b[i].upper()]
  sc.append((v,m))
 return sorted(sc,reverse=True)
def S(st,d,a,b,ply,rm=None):
 global N;N+=1
 if N>=NB:raise TO
 bd,s=st[0],st[1];kc="K"if s>0 else"k"
 if kc not in bd:return-1e5+ply
 qm=d<=0 and not A(bd,bd.index(kc),-s);tt=None
 if qm:
  best=s*E(st)
  if best>=b:return b
  a=max(a,best)
 else:
  en=T.get(st)
  if en and en[0]>=d and ply>0:
   if en[1]==0:return en[2]
   if en[1]==1:a=max(a,en[2])
   else:b=min(b,en[2])
   if a>=b:return en[2]
  tt=en[3]if en else None
  best=-9e9
 a0=a;bm=None
 for _,m in O(st,G(st,1)if qm else(rm if rm else G(st,0)),tt):
  st2=M(st,m)
  if A(st2[0],st2[0].index(kc),-s):continue
  v=-S(st2,d-1,-b,-a,ply+1)
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:break
 if bm is None:
  if qm:return best
  return(-1e5+ply)if A(bd,bd.index(kc),-s)else 0
 if not qm:T[st]=(d,1 if best>=b else(2 if best<=a0 else 0),best,bm)
 if ply==0:BM[0]=bm
 return best
def V(m):return"".join("abcdefgh"[x%10-1]+str(10-x//10)for x in m[:2])+m[2]
def K(g):
 global N
 st=F(g["fen"])
 ms=[m for m in G(st,0)if V(m)in g["legal_moves"]]
 T.clear();N=0;BM[0]=ms[0]
 for d in range(1,100):
  try:S(st,d,-9e9,9e9,0,ms)
  except TO:break
 return V(BM[0])
g=P("/game",{})
while g["status"]!="done":
 while g["status"]=="your_move":
  try:mv=K(g)
  except:mv=g["legal_moves"][0]
  g=P("/move",{"game":g["game"],"move":mv})
 g=P("/game",{})