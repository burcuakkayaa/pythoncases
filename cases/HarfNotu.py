class HarfNotu:

    def harf_notu(self, toplam_not):
        if toplam_not >= 90:
            return 'AA'
        elif toplam_not >= 85:
            return 'BA'
        elif toplam_not >= 80:
            return 'BB'
        elif toplam_not >= 75:
            return 'CB'
        elif toplam_not >= 70:
            return 'CC'
        elif toplam_not >= 65:
            return 'DC'
        elif toplam_not >= 60:
            return 'DD'
        elif toplam_not >= 55:
            return 'FD'
        else:
            return 'FF'

    def ders_notları(self, vize1, vize2, final):
        if 0 < vize1 < 100 and 0 < vize2 < 100 and 0 < final < 100:
            toplam_not = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
            print(toplam_not)
            print(self.harf_notu(toplam_not))
        else:
            print("Lütfen notlarınızı 0 ile 100 arasında giriniz..")


def main():
    notlar = HarfNotu()
    notlar.ders_notları(80, 80, 80)


if __name__ == "__main__":
    main()
