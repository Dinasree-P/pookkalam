from joy import *

A = circle(r=150, fill='GREEN')
B = circle(r=145, fill='#36013F', stroke="RED", stroke_width=3)
C = ellipse(w=280,h=30,fill="WHITE",stroke="NONE")|repeat(30,rotate(20))
D = C|repeat(4,rotate(15))
E = ellipse(w=260, h=90, fill="YELLOW", stroke="black")|repeat(9,rotate(angle=20))
F = circle(r=55, fill="#66B032", stroke="none")
G = ellipse(w=100,h=11,fill="#FF8C00",stroke="BROWN")|repeat(20,rotate(25))
H = G|repeat(3,rotate(15))
I = circle(r=40, fill="WHITE",STROKE="NONE")
J=rectangle(w=50,h=50,fill="yellow",stroke='black') | repeat(30,rotate(15))
K=rectangle(w=40,h=40,fill="orange",stroke='black') | repeat(10,rotate(30))

L= rectangle(w=60,h=60,fill="#a10000",stroke="black") | rotate(15) | repeat(10, rotate(10))

M = rectangle(w=159,h=159,fill="#e64805",stroke="black") | rotate(20) | repeat(10, rotate(10))

N = rectangle(w=90,h=94,fill="#ffd503",stroke="black") | rotate(30) | repeat(10, rotate(10))

O = rectangle(w=152,h=152,fill="#ffee6b",stroke="black") | rotate(35) | repeat(10, rotate(10))

P = rectangle(w=140,h=140,fill="#fffded",stroke="black") | rotate(40) | repeat(10, rotate(10))

Q=rectangle(w=130,h=130,fill="#FFC300",stroke='black') | repeat(40,rotate(36))

R=ellipse(w=70,h=20,x=30,fill="#FF5733",stroke="black")|repeat(24,rotate(15))

S=ellipse(w=70,h=20,x=30,fill="#C70039 ",stroke="black")|repeat(12,rotate(30))
T=ellipse(w=55,h=15,x=15,fill="#900C3F",stroke="black")|repeat(12,rotate(30))
U= circle(r=30,fill="purple",stroke="none")
V = circle(r=25, fill="blue", stroke="none")
W = ellipse(w=40, h=9,fill="red",stroke="white")|repeat(6 , rotate(30))
X = circle(r=8 , fill="#E5E4E2")

show(A,B,C,D,E,X,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X)
