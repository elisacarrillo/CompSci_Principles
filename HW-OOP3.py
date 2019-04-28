class Shape:
    def arearandom(self,y):
        self.y = y
    def areaShape(self, y):
        y = 0
        return(0)
class Square(Shape):
    def __init__(self,y):
        self.y = y
    def areasquare(self):
        areas = self.y * self.y
        print("The area of the square is " + str(areas))


