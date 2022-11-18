class Rectangle():
    def __init__(self, Length, Width):
        self.Length=Length
        self.Width=Width

    def perimeter(self):
        perimeter_res = (2* self.Length)+(2*self.Width)
        print (perimeter_res)

    def area(self):
        area_res=self.Length*self.Width
        print(area_res)
