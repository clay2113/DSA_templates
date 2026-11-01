#Dot product 
def dot(x1,y1,x2,y2):
    #NittinS Snippets
    return x1*x2+y1*y2
#for non origin-originating vectors
def dot(x1,y1,x2,y2,x3,y3,x4,y4):
    #NittinS Snippets
    return (x2-x1)*(x4-x3)+(y2-y1)*(y4-y3)

#CROSS PRODUCT FOR NON ORIGIN-ORIGINATING VECTORS
def cross(ax,ay,bx,by):
    return ax*by-ay*bx

#CROSS PRODUCT FOR THREE POINTS WHICH REPRESENTS A TWO VECTOR
def cross(A,B,C):
    return (B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
