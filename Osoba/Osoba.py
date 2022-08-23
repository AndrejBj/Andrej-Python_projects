# predstavlja sve osobe u informacionom sistemu fakulteta
class Osoba:
    def __init__(self, ime, prezime, jmbg):   
        self.__ime = ime
        self.__prezime = prezime
        self.__jmbg = jmbg
 
    def __str__(self):                        
        return '{} {} {}'.format(self.__ime, self.__prezime,self.__jmbg)  
 
    def predstavi_se(self):
        print('Ja sam', self.__ime, self.__prezime)   
 
# predstavlja osobe zaposlene na fakultetu
class Zaposleni(Osoba): 
    def __init__(self, ime, prezime, jmbg, plata, soba, telefon):
        super().__init__(ime, prezime, jmbg) 
        self.__plata = plata
        self.__soba = soba
        self.__telefon = telefon
 
    def __str__(self):
        return super().__str__() + '\n' + str(self.__plata) + \
            ' soba: ' + self.__soba + ' tel: ' + self.__telefon
 
    def promeni_platu(self, nova):
        self.__plata = nova
 
# predstavlja studente na fakultetu
class Student(Osoba): 
    def __init__(self, ime, prezime, jmbg, indeks, smer):
        super().__init__(ime, prezime, jmbg) 
        self.__indeks = indeks
        self.__godina = 1
        self.__smer = smer
 
    def __str__(self):
        return super().__str__() + '\n' + self.__indeks + \
            ' godina: ' + str(self.__godina) + ' smer: ' + self.__smer
 
    def upisi_godinu(self, godina):
        if godina < 6 and (godina == self.__godina or 
                           godina == self.__godina + 1):
            self.__godina = godina