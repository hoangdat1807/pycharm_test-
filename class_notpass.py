class Sieunhan :
    def __init__(self, pa_ten ,pa_tuoi, pa_vu_khi):
        """ham constructor(initialize method )nhằm tạo ra một khuôn mẫu
                                                      và truyền các thuộc tình vào ,còn việc gán giá trị thì để khuôn 
                                                      mẫu làm """
        self.ten= "Sieunhan" + pa_ten      # từ khóa self nhan gia trị chính là đối tượng của hàm đó
        self.tuoi= pa_tuoi
        self.vukhi= pa_vu_khi
Sieu_nhan_A= Sieunhan("Dat", "21", "Kiem" )
"""từ khóa self được gán với object "Sieu_nhan_A" và các agumen
Dat ,21, kiem được truyền vào theo thứ tự """
print ("tên của Sieu nhân", Sieu_nhan_A. ten )
print("tuổi của Siêu nhân ", Sieu_nhan_A.tuoi)
print("vũ khí của Siêu nhân", Sieu_nhan_A.vukhi)

    def xinchao(self)
        