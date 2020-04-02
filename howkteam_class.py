class Sieunhan :
    def __init__(self,para_ten, para_mausac, para_vukhi ):
        self.ten= "power " + para_ten
        self.mausac= para_mausac
        self.vukhi=  para_vukhi
    def xinchao(self):
        return "xin chao SN " + self.ten
Sieu_nhan_A= Sieunhan("do", "Do", "kiem")
print (Sieu_nhan_A. xinchao())
