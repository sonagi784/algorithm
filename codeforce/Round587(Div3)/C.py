# union(W, B1) + union(W, B2) - union(W, B1, B2) = W
W = list(map(int, input().split()))
B1 = list(map(int, input().split()))
B2 = list(map(int, input().split()))
 
def union(A, B, C=None):
    # x1, y1 = [0][1] / x2, y2 = [2][3]
    # W_x1 < B_x2 and W_x2 > B_x1 , y1<y2 and y2>y1
    Aleft, Abottom, Aright, Atop = A
    Bleft, Bbottom, Bright, Btop = B
    if C != None:
        Cleft, Cbottom, Cright, Ctop = C
        if (Bleft < Cright and Bright > Cleft) and (Bbottom < Ctop and Btop > Cbottom):
            Bleft = max(Bleft, Cleft)
            Bright = min(Bright, Cright)
            Bbottom = max(Bbottom, Cbottom)
            Btop = min(Btop, Ctop)
        else:
            Bleft, Bbottom, Bright, Btop = 0, 0, 0, 0
    if (Aleft < Bright and Aright > Bleft) and (Abottom < Btop and Atop > Bbottom):
        width = min(Aright, Bright) - max(Aleft, Bleft)
        height = min(Atop, Btop) - max(Abottom, Bbottom)
        return width*height
    else:
        return 0
 
if union(W, B1) + union(W, B2) - union(W, B1, B2) == (W[2]-W[0]) * (W[3]-W[1]):
    print('NO')
else:
    print('YES')