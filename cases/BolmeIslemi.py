class BolmeIslemi:

    def bolunen_sayi_bulma(self, min_sayi, max_sayi, bolen_sayi):
        self.min_sayi = min_sayi
        self.max_sayi = max_sayi
        self.bolen_sayi = bolen_sayi
        tam_bolunenler = []

        for sayi in range(self.min_sayi, self.max_sayi):
            kalan = sayi % self.bolen_sayi
            if kalan == 0:
                tam_bolunenler.append(sayi)

        return tam_bolunenler


d = BolmeIslemi()
print(d.bolunen_sayi_bulma(1, 200, 12))
