# a: int = 596
# score2 : float = 98.5
# hobby2 : str = "Python"
# flag2:bool = True
# pic:None = None
#
# names = ["A","C","E"]
# phones = {"13393780667"}
# options = {"count":2,"sum":3}
# goods =("手机",18888,3)

def circle_area_len(r:float=0)->tuple[float,float]:
    return round(3.14*r*r,1),round(2*3.14*r,1)

al = circle_area_len(10.8)
print(al)