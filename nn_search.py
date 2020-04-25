import math

global distance
global distance2

distance = 100000
point = (0,0)

def find_nearest(tree,p):
    global distance
    global point
    x2 = int(p[0])
    y2 = int(p[1])

    if tree == None or tree == 'None' or tree == []:
        print( 'No tree Available' )
    elif tree[0] == p:
            print( 'point lies on tree')
    elif tree[0]>p:
        x1 = int(tree[0][0])
        y1 = int(tree[0][1])
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if dist < distance:
            distance = dist
            point = tree[0]
        if isinstance(tree[1], tuple):
            find_nearest(tree[1],p)
            n = [distance,point]
            print("Point does not lie on tree")
            print("Distance from closest point:",n[0])
            print("Closest point",n[1])
        
    elif tree[0]<p:
        x1 = int(tree[0][0])
        y1 = int(tree[0][1])
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if dist < distance:
            distance = dist
            point = tree[0]
        if isinstance(tree[2], tuple):
            find_nearest(tree[2],p)
            n = [distance,point]
            print("Point does not lie on tree")
            print("Distance from closest point:",n[0])
            print("Closest point",n[1])
        

