class people :
    def __init__(self, Ten ,Tuoi, nghe_nghiep ):
        self.dinhdanh = Ten
        self.tuoi = Tuoi
        self.nghe =nghe_nghiep
    def xinchao(self):
        return "Xin chao cac ban Python"+ self.dinhdanh

Sieunhan= people( "Đạt ", "21", "CEO Group")

print (Sieunhan.xinchao())

