# area or circumstance in circle
import math
def circle(r):
    area=round(math.pi*r*r,2)
    circumstance=round(2*math.pi*r,2)
    return area,circumstance
ar,cir=circle(3)
print("Area: ",ar,"\n" "Circumstance: ",cir)

