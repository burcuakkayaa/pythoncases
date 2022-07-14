
class Sayilar:

    def sayi_atama(self, sayi):

        if sayi > 9 and sayi < 100:
            count = 0
            result = []

            while sayi != 0:
                deger = sayi % 10
                result.append(self.__sayi_okunusu(deger, count))
                count += 1
                sayi = int(sayi/10)

            print(*reversed(result))
        else:
            print("Please enter a valid number")


    def __sayi_okunusu(self, rakam, basamak_yeri):

        ilk_basamak = {0: "", 1: "bir", 2: "iki", 3: "üc", 4: "dört",
                       5: "bes", 6: "altı", 7: "yedi", 8: "sekiz",
                       9: "dokuz"}
        ikinci_basamak = {1: "on", 2: "yirmi", 3: "otuz", 4: "kırk",
                          5: "elli", 6: "altmıs", 7: "yetmis",
                          8: "seksen", 9: "doksan"}


        basamak_list = [ilk_basamak, ikinci_basamak]

        return basamak_list[basamak_yeri][rakam]



def main():


    sayilar_class = Sayilar()
    sayilar_class.sayi_atama(70)


if __name__ == "__main__":
    main()
