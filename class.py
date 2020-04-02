class Baitaptinhtichchuoi:
    def __init__(self , list ):
        self.list_item= list
        self.mul_item= 1
    def mul(self):
        for x in self.list_item :
            self.mul_item *=x
list=[2,4,5,6,7]
p1 = Baitaptinhtichchuoi(list)
p1.mul()
print (p1.mul_item)