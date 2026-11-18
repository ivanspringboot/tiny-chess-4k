import os,json,random,sys,urllib.request
aG=(33,31,18,14,-33,-31,-18,-14)
aF=(1,-1,16,-16,15,17,-15,-17)
ax=(15,17,-15,-17)
ay=(1,-1,16,-16)
aU=ax+ay
U=100000
CAP0 = 40000
aH=(0,100,320,330,500,900,0)
bd=lambda G:(0,100,320,330,500,900,0,100,320,330,500,900,0)[G]
h=[0]*128
q=[[],[]]
j=[0,0]
g=0
o=0
u=0
L=0
f=0
ar=[]
am=[0]*128
I=None
Q=None
aj=None
be=None
F=None
ad=0
ak=None
V=None
N=None
w=0
H=0
R={}
X=0
Y=0
W=0
B=0
av=0
def init():
 global aj,F,ad,ak,V,N,I,Q,ac,ab
 M=random.Random(0x5EED2026)
 aj=[[0]*128 for _ in range(10)]
 aI=(0,0,4,8,14,24,40,0)
 aL=(0,0,0,10,15,10,5,0)
 bg=(100,320,330,500,900)
 def aT(d,x):
  b,D=x&7,x>>3
  y=min(b,7-b)+min(D,7-D)
  if d==1:
   return 100+aI[D]+(aL[D]if b in(3,4)else 0)
  if d==2:
   return 320+6*y-20
  if d==3:
   return 330+4*y-8
  if d==4:
   return 500+(15 if D==6 else 0)+(5 if D==0 and b in(3,4)else 0)
  return 900+2*y-6
 aZ=(20,25,10,0,0,10,25,20)
 ac=[0]*64
 ab=[0]*64
 for x in range(64):
  b,D=x&7,x>>3
  ac[x]=aZ[b]if D==0 else max(-50,-15*D)
  ab[x]=8*(min(b,7-b)+min(D,7-D))-24
 for p in range(128):
  if p&0x88:
   continue
  b,aR=p&15,p>>4
  for y in(0,1):
   x=aR*8+b if y==0 else(7-aR)*8+b
   for d in range(1,6):
    aj[y*5+d-1][p]=aT(d,x)
 F=[[M.getrandbits(64)for _ in range(128)]for _ in range(12)]
 ad=M.getrandbits(64)
 ak=[M.getrandbits(64)for _ in range(16)]
 V=[M.getrandbits(64)for _ in range(128)]
 N=[0]*128
 N[0]=2
 N[7]=1
 N[112]=8
 N[119]=4
 I=[[0,0]for _ in range(96)]
 Q=[[0]*128 for _ in range(12)]
def add(p,i):
 global X,Y,W,B
 y=0 if i<7 else 1
 d=i-6*y
 if d==6:
  return
 aC=1 if y==0 else-1
 X+=aC*aj[y*5+d-1][p]
 if d!=1:
  Y+=(320,330,500,900)[d-2]
 if d==3:
  if y:
   B+=1
  else:
   W+=1
def rem(p,i):
 global X,Y,W,B
 y=0 if i<7 else 1
 d=i-6*y
 if d==6:
  return
 aC=1 if y==0 else-1
 X-=aC*aj[y*5+d-1][p]
 if d!=1:
  Y-=(320,330,500,900)[d-2]
 if d==3:
  if y:
   B-=1
  else:
   W-=1
def setup(K):
 global h,q,j,g,o,u,L,f,ar,X,Y,W,B
 h=[0]*128
 q=[[],[]]
 X=Y=W=B=0
 i=K.split()
 M=7
 b=0
 for O in i[0]:
  if O=="/":
   M-=1
   b=0
  elif O.isdigit():
   b+=int(O)
  else:
   y=1 if O.islower()else 0
   z="pnbrqk".index(O.lower())+1+6*y
   p=M*16+b
   h[p]=z
   q[y].append(p)
   add(p,z)
   if z-6*y==6:
    j[y]=p
   b+=1
 g=0 if i[1]=="w" else 1
 u=0
 if len(i)>2:
  for O in i[2]:
   u|={"K":1,"Q":2,"k":4,"q":8}.get(O,0)
 o=0
 if len(i)>3 and i[3]!="-":
  o=(int(i[3][1])-1)*16+"abcdefgh".index(i[3][0])
 L=0
 ar=[]
 f=0
 for y in(0,1):
  for p in q[y]:
   f^=F[h[p]-1][p]
 if g:
  f^=ad
 f^=ak[u]
 if o:
  f^=V[o]
def atk(p,y):
 aE=y*6
 if y==0:
  c=p-15
  if 0<=c<128 and not c&0x88 and h[c]==1:
   return 1
  c=p-17
  if 0<=c<128 and not c&0x88 and h[c]==1:
   return 1
 else:
  c=p+15
  if 0<=c<128 and not c&0x88 and h[c]==7:
   return 1
  c=p+17
  if 0<=c<128 and not c&0x88 and h[c]==7:
   return 1
 for t in aG:
  c=p+t
  if 0<=c<128 and not c&0x88 and h[c]==2+aE:
   return 1
 for t in aF:
  c=p+t
  if 0<=c<128 and not c&0x88 and h[c]==6+aE:
   return 1
 for t in ax:
  c=p+t
  while not c&0x88:
   i=h[c]
   if i:
    if i==3+aE or i==5+aE:
     return 1
    break
   c+=t
 for t in ay:
  c=p+t
  while not c&0x88:
   i=h[c]
   if i:
    if i==4+aE or i==5+aE:
     return 1
    break
   c+=t
 return 0
def gen(a,al=0):
 l=[]
 ao=16-32*a
 az=6*a
 for b in q[a]:
  d=h[b]-az
  if d==1:
   c=b+ao
   if not c&0x88 and not h[c]:
    if c<8 or c>111:
     l+=[b|c<<7|i<<14 for i in(5,4,3,2)]
    elif al:
     pass
    else:
     l.append(b|c<<7)
     if b>>4==(1 if a==0 else 6):
      bc=c+ao
      if not bc&0x88 and not h[bc]:
       l.append(b|bc<<7)
   for c in(b+ao-1,b+ao+1):
    if c&0x88:
     continue
    G=h[c]
    if G:
     if(G>6)!=a:
      if c<8 or c>111:
       l+=[b|c<<7|i<<14 for i in(5,4,3,2)]
      else:
       l.append(b|c<<7)
    elif o and c==o:
     l.append(b|c<<7)
  elif d==2:
   for t in aG:
    c=b+t
    if not c&0x88:
     G=h[c]
     if G:
      if(G>6)!=a:
       l.append(b|c<<7)
     elif not al:
      l.append(b|c<<7)
  elif d==6:
   for t in aF:
    c=b+t
    if not c&0x88:
     G=h[c]
     if not G or(G>6)!=a:
      l.append(b|c<<7)
   if b==j[a]and not al:
    if a==0:
     if u&1 and not h[5]and not h[6]and not atk(4,1)and not atk(5,1)and not atk(6,1):
      l.append(4|6<<7)
     if u&2 and not h[3]and not h[2]and not h[1]and not atk(4,1)and not atk(3,1)and not atk(2,1):
      l.append(4|2<<7)
    else:
     if u&4 and not h[117]and not h[118]and not atk(116,0)and not atk(117,0)and not atk(118,0):
      l.append(116|118<<7)
     if u&8 and not h[115]and not h[114]and not h[113]and not atk(116,0)and not atk(115,0)and not atk(114,0):
      l.append(116|114<<7)
  else:
   if d==3:
    aA=ax
   elif d==4:
    aA=ay
   else:
    aA=aU
   for t in aA:
    c=b+t
    while not c&0x88:
     G=h[c]
     if G:
      if(G>6)!=a:
       l.append(b|c<<7)
      break
     if not al:
      l.append(b|c<<7)
     c+=t
 return l
def mk(n):
 global o,u,L,f,g
 b=n&127
 d=n>>7&127
 ap=n>>14&15
 i=h[b]
 a=0 if i<7 else 1
 m=h[d]
 ar.append((n,m,u,o,L,f))
 f^=F[i-1][b]^F[i-1][d]
 h[b]=0
 q[a].remove(b)
 h[d]=i
 q[a].append(d)
 rem(b,i)
 add(d,i)
 if m:
  q[1-a].remove(d)
  f^=F[m-1][d]
  rem(d,m)
 if ap:
  ah=ap+6*a
  f^=F[i-1][d]^F[ah-1][d]
  rem(d,i)
  h[d]=ah
  add(d,ah)
 elif i-6*a==1 and o and d==o:
  c=d-16+32*a
  m=h[c]
  h[c]=0
  q[1-a].remove(c)
  f^=F[m-1][c]
  rem(c,m)
 elif i-6*a==6:
  s=-1
  if d-b==2:
   s,ai=b+3,b+1
  elif b-d==2:
   s,ai=b-4,b-1
  if s>=0:
   J=h[s]
   h[s]=0
   h[ai]=J
   q[a].remove(s)
   q[a].append(ai)
   f^=F[J-1][s]^F[J-1][ai]
   rem(s,J)
   add(ai,J)
  j[a]=d
 aP=u
 if i-6*a==6:
  u&=~(3<<(2*a))
 u&=~(N[b]|N[d])
 if u!=aP:
  f^=ak[aP]^ak[u]
 A=o
 o=0
 if A:
  f^=V[A]
 if i-6*a==1 and(d-b==32 or b-d==32):
  o=(b+d)>>1
  f^=V[o]
 if i-6*a==1 or m:
  L=0
 else:
  L+=1
 g^=1
 f^=ad
 return m
def unmk():
 global o,u,L,f,g,j
 n,m,u,o,L,f=ar.pop()
 b=n&127
 d=n>>7&127
 ap=n>>14&15
 i=h[d]
 a=0 if i<7 else 1
 g=a
 h[b]=i
 h[d]=0
 q[a].remove(d)
 q[a].append(b)
 rem(d,i)
 add(b,i)
 if ap:
  h[b]=1+6*a
  rem(b,i)
  add(b,h[b])
 if m:
  h[d]=m
  q[1-a].append(d)
  add(d,m)
 elif i-6*a==1 and o and d==o:
  c=d-16+32*a
  h[c]=1+6*(1-a)
  q[1-a].append(c)
  add(c,h[c])
 if i-6*a==6:
  s=-1
  if d-b==2:
   s,ai=b+3,b+1
  elif b-d==2:
   s,ai=b-4,b-1
  if s>=0:
   J=h[ai]
   h[s]=J
   h[ai]=0
   q[a].remove(ai)
   q[a].append(s)
   rem(ai,J)
   add(s,J)
  j[a]=b
aa=6400
def ev():
 global W,B
 i=Y
 if i>aa:
  i=aa
 G=aa-i
 aN,aM=j[0],j[1]
 aS=(aN>>4)*8+(aN&7)
 aQ=(7-(aM>>4))*8+(aM&7)
 an=((ac[aS]*i+ab[aS]*G+3200)//aa)-((ac[aQ]*i+ab[aQ]*G+3200)//aa)
 z=X+an
 if W>1:
  z+=30
 if B>1:
  z-=30
 return z if g==0 else-z
def srt(l,at,e):
 aX,aY=I[e]
 B=h
 aW=Q
 aD=[]
 for n in l:
  b=n&127
  G=B[n>>7&127]
  if n==at:
   p=1<<40
  elif G:
   p=(1<<32)+100*(aH[G&7]if G&7<7 else 0)-(aH[B[b]&7]if B[b]&7<7 else 0)//20+(n>>14)*900
  elif n>>14:
   p=(1<<30)+(n>>14)
  elif n==aX:
   p=1<<29
  elif n==aY:
   p=(1<<29)-1
  else:
   i=B[b]
   p=aW[i-1][n>>7&127]if i else 0
  aD.append((p,n))
 aD.sort(reverse=True)
 return[n for p,n in aD]
def qs(s,v,e):
 global w
 w+=1
 if w>H:
  raise OverflowError
 S=e-av
 if S>8:
  return ev()
 a=g
 C=atk(j[a],a^1)
 if C:
  p=-U*2
  l=gen(a)
 else:
  p=ev()
  if p>=v:
   return p
  if p>s:
   s=p
  if p+1100<=s:
   return s
  l=gen(a,1)
  if S>1:
   l=[n for n in l if n>>14 or bd(h[n>>7&127])+120>=bd(h[n&127])]
 ag=0
 for n in srt(l,0,e):
  mk(n)
  if atk(j[a],a^1):
   unmk()
   continue
  ag+=1
  z=-qs(-v,-s,e+1)
  unmk()
  if z>s:
   s=z
   if z>=v:
    return z
 if C and ag==0:
  return-U+e
 return s
def ne(t,s,v,e,aO):
 global w,f,g,o
 w+=1
 if w>H:
  raise OverflowError
 if L>=100:
  return 0
 for bf in range(e-1,-1,-2):
  if am[bf]==f:
   return 0
 am[e]=f
 a=g
 C=atk(j[a],a^1)
 if C and e<56:
  t+=1
 if t<=0 or e>=56:
  global av
  av=e
  return qs(s,v,e)
 P=R.get(f)
 at=0
 if P:
  at=P[3]
  if P[0]>=t:
   if P[2]==2:
    return P[1]
   if P[2]==1 and P[1]>=v:
    return P[1]
   if P[2]==0 and P[1]<=s:
    return P[1]
 if aO and t>=3 and not C:
  ag=0
  for p in q[a]:
   d=h[p]-6*a
   if d!=1 and d!=6:
    ag+=1
  if ag>3:
   A=o
   o=0
   if A:
    f^=V[A]
   g^=1
   f^=ad
   z=-ne(t-3,-v,-v+1,e+1,0)
   f^=ad
   g^=1
   o=A
   if A:
    f^=V[A]
   if z>=v:
    am[e]=0
    return v
 aV=s
 l=gen(a)
 r=-U*2
 aK=0
 ag=0
 for n in srt(l,at,e):
  b=n&127
  d=n>>7&127
  m=h[d]or(1 if(n>>14==0 and h[b]-6*a==1 and o and d==o)else 0)
  mk(n)
  if atk(j[a],a^1):
   unmk()
   continue
  ag+=1
  if ag==1:
   z=-ne(t-1,-v,-s,e+1,1)
  else:
   M=0
   if t>=3 and ag>3 and not m and not C and not n>>14:
    M=1 if(t<6 or ag<9)else 2
   z=-ne(t-1-M,-s-1,-s,e+1,1)
   if z>s and M:
    z=-ne(t-1,-s-1,-s,e+1,1)
   if s<z<v:
    z=-ne(t-1,-v,-s,e+1,1)
  unmk()
  if z>r:
   r=z
   aK=n
   if z>s:
    s=z
    if z>=v:
     if not m and not n>>14:
      an=I[e]
      if an[0]!=n:
       an[1]=an[0]
       an[0]=n
      Q[h[b]-1][d]+=t*t
     break
 if ag==0:
  return-U+e if C else 0
 A=R.get(f)
 if A is None or t>=A[0]or A[2]!=2:
  R[f]=(t,r,0 if r<=aV else 1 if r>=v else 2,aK)
 return r
def uci(n):
 b=n&127
 d=n>>7&127
 p="abcdefgh"[b&15]+str((b>>4)+1)+"abcdefgh"[d&15]+str((d>>4)+1)
 if n>>14:
  p+="nbrq"[(n>>14)-2]
 return p
def ba(Z):
 b="abcdefgh".index(Z[0])+(int(Z[1])-1)*16
 return b|("abcdefgh".index(Z[2])+(int(Z[3])-1)*16)<<7|((("nbrq".index(Z[4])+2)<<14)if len(Z)>4 else 0)
def think(K,T,af=(),aB=None):
 global w,H,R,f,h,q,j,g,o,u,L,ar,am,X,Y,W,B
 setup(K)
 R={}
 am=[0]*128
 for an in I:
  an[0]=an[1]=0
 H=int(os.environ.get("CAP","0"))or CAP0
 E=None
 if len(af)>3:
  E={}
  setup(aB or K)
  for Z in af:
   mk(ba(Z))
   E[f]=E.get(f,0)+1
  setup(K)
  R={}
 r=0
 w=0
 for t in range(1,30):
  k=(h[:],q[0][:],q[1][:],j[:],g,o,u,L,f,X,Y,W,B)
  try:
   ne(t,-U*2,U*2,0,1)
  except OverflowError:
   h[:]=k[0]
   q[0][:],q[1][:]=k[1],k[2]
   j[:]=k[3]
   g,o,u,L,f=k[4],k[5],k[6],k[7],k[8]
   X,Y,W,B=k[9],k[10],k[11],k[12]
   ar.clear()
   break
  P=R.get(f)
  if P and P[2]==2:
   r=P[3]
 bb=set(T)
 aq=E is not None and R.get(f,(0,0,0,0))[1]>0
 ae=None
 for n in srt(gen(g),r,0):
  Z=uci(n)
  if Z not in bb:
   continue
  mk(n)
  aJ=atk(j[1-g],g)
  M=aq and E.get(f,0)>1
  unmk()
  if aJ:
   continue
  if not M:
   return Z
  if ae is None:
   ae=Z
 return ae or T[0]
def main():
 init()
 aw=os.environ["MAKEFUN_ENV_URL"]
 while True:
  M=urllib.request.Request(aw+"/game",b"{}",{"content-type":"application/json"})
  au=json.load(urllib.request.urlopen(M))
  if au.get("status")=="done":
   return
  while au.get("status")=="your_move":
   n=think(au["fen"],au["legal_moves"],au.get("moves")or(),au.get("start_fen"))
   M=urllib.request.Request(aw+"/move",json.dumps({"game":au["game"],"move":n}).encode(),{"content-type":"application/json"})
   au=json.load(urllib.request.urlopen(M))
main()

