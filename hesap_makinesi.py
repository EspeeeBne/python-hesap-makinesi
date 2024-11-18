import math

def get_valid_double_input():
    while True:
        try:
            return float(input())
        except ValueError:
            print("Hata: Geçerli bir sayı girin: ", end="")

def main():
    devam = True
    islem_gecmisi = []

    while devam:
        print("Hesap Makinesi\n")
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Üüs Alma")
        print("6. Karekök Alma")
        print("7. Ortalama Hesaplama")
        print("8. Faktoriyel Hesaplama")
        print("9. Geçmiş İşlemleri Görüntüle")
        print("Çıkmak için q'ya basın\n")

        secim = input("Seçiminizi yapın: ")

        if secim.lower() == "q":
            devam = False
            break

        sonuc = 0
        gecerli_islem = True

        if secim == "1":
            print("Birinci sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            print("İkinci sayıyı girin: ", end="")
            sayi2 = get_valid_double_input()

            sonuc = sayi1 + sayi2
            islem_gecmisi.append(f"{sayi1} + {sayi2} = {sonuc}")
        elif secim == "2":
            print("Birinci sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            print("İkinci sayıyı girin: ", end="")
            sayi2 = get_valid_double_input()

            sonuc = sayi1 - sayi2
            islem_gecmisi.append(f"{sayi1} - {sayi2} = {sonuc}")
        elif secim == "3":
            print("Birinci sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            print("İkinci sayıyı girin: ", end="")
            sayi2 = get_valid_double_input()

            sonuc = sayi1 * sayi2
            islem_gecmisi.append(f"{sayi1} * {sayi2} = {sonuc}")
        elif secim == "4":
            print("Birinci sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            print("İkinci sayıyı girin: ", end="")
            sayi2 = get_valid_double_input()

            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                islem_gecmisi.append(f"{sayi1} / {sayi2} = {sonuc}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez.\n")
                gecerli_islem = False
        elif secim == "5":
            print("Taban sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            print("Üös değerini girin: ", end="")
            us = get_valid_double_input()

            sonuc = math.pow(sayi1, us)
            islem_gecmisi.append(f"{sayi1} ^ {us} = {sonuc}")
        elif secim == "6":
            print("Sayıyı girin: ", end="")
            sayi1 = get_valid_double_input()

            if sayi1 >= 0:
                sonuc = math.sqrt(sayi1)
                islem_gecmisi.append(f"√{sayi1} = {sonuc}")
            else:
                print("Hata: Negatif bir sayının karekökü alınamaz.\n")
                gecerli_islem = False
        elif secim == "7":
            print("Kaç sayı gireceksiniz?: ", end="")
            adet = int(get_valid_double_input())
            toplam = 0

            for i in range(1, adet + 1):
                print(f"{i}. sayıyı girin: ", end="")
                toplam += get_valid_double_input()

            sonuc = toplam / adet
            islem_gecmisi.append(f"Girilen {adet} sayının ortalaması = {sonuc}")
        elif secim == "8":
            print("Faktoriyelini almak istediğiniz sayıyı girin: ", end="")
            faktoriyel_sayisi = int(get_valid_double_input())
            sonuc = 1

            for i in range(1, faktoriyel_sayisi + 1):
                sonuc *= i

            islem_gecmisi.append(f"{faktoriyel_sayisi}! = {sonuc}")
        elif secim == "9":
            print("Geçmiş İşlemler:")
            for islem in islem_gecmisi:
                print(islem)
        else:
            print("Geçersiz seçim. Lütfen 1-9 arasında bir seçim yapın.\n")
            gecerli_islem = False

        if gecerli_islem and secim != "9":
            print(f"Sonuç: {sonuc}\n")

    print("Programdan çıkılıyor. Görüşürüz!")

if __name__ == "__main__":
    main()
