import random

def bn():
    while True:
        pilih= int(input("Apa yang ingin anda lakukan, 1: Fakta seputar sampah | 2: Pemilah sampah"))
        if pilih == 1:
            
            Choices=['Setiap hari, manusia menghasilkan sekitar 2.0 miliar ton sampah di seluruh dunia.', 'Indonesia menghasilkan sekitar 64 juta ton sampah per tahun, dengan 17% di antaranya adalah sampah plastik.', 'Setiap orang di Indonesia menghasilkan rata-rata 0,7 kg sampah per hari.', 'Sampah plastik di laut dapat membunuh lebih dari 1 juta hewan laut setiap tahun.', 'Sampah yang menumpuk di TPA Tempat Pemrosesan Akhir dapat menghasilkan gas metana, yang berkontribusi terhadap perubahan iklim.', 'Sampah yang tidak dikelola dengan baik dapat mencemari tanah dan air, membahayakan kesehatan manusia dan lingkungan.']
            print(random.choice(Choices))
            print("Sumber: bard.com")
        if pilih == 2:
            print("Aku adalah bot pemilih sampah organik atau anorganik")
            sampah= input("Apa nama sampah nya? (Gunakan huruf kapital)")
            if sampah=='MAKANAN' or sampah=='KULIT' or sampah=='DAUN' or sampah=='TULANG' or sampah=='KERTAS ' or sampah=='TISU' or sampah=='RUMPUT':
                print("Sampah tersebut termasuk sampah organik")
            else:
                print("Sampah tersebut termasuk sampah anorganik")

bn()