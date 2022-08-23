# definise apstraktni tip koji predstavlja vlasnike stanova
class Vlasnik:
 
    def __init__(self, ime, prezime, jmbg):
        self.__ime = ime
        self.__prezime = prezime
        self.__jmbg = jmbg
 
    def __str__(self):
        return '{} {} {}'.format(self.__ime,self.__prezime, self.__jmbg)
 
    def jmbg(self):
        return self.__jmbg
 
# da li ime ili prezime sadrzi kljucnu rec
    def ime_sadrzi(self, upit):
        ime_ok = self.__ime.find(upit) != -1            
        prezime_ok = self.__prezime.find(upit) != -1    
        return ime_ok or prezime_ok
 
# definise tip koji predstavlja stanove
class Stan:
 
    def __init__(self, m2, sprat):
        self.__m2 = m2
        self.__sprat = sprat
        self.__vlasnik = None          
 
    def __str__(self):
         st = '{}m2 spr. {}'.format(self.__m2, self.__sprat)
         return '{}. {}'.format(st, str(self.__vlasnik))
 
    def vlasnik(self):                   
        return self.__vlasnik           
 
    def promeni_vlasnika(self, novi_vlasnik):
        self.__vlasnik = novi_vlasnik         
 
    def površina(self):
        return self.__m2
 
 # definise apstraktni tip koji predstavlja stambenu zgradu
class Zgrada:
 
    def __init__(self, adresa, stanovi):
        self.__adresa = adresa
        self.__stanovi = stanovi      
 
    def __str__(self):
        opis = []
        for stan in self.__stanovi:   
            opis.append(str(stan))
        return '{}\n---\n{}\n---\n'.format(self.__adresa, opis)
 
    def dodaj_stan(self, stan):
        self.__stanovi.append(stan)
 
# vraca recnik sa vlasnicima koji zadovoljavaju upit i njihovim stanovima tj trazimo ovde po imenu vlasnika koje sve stanove poseduje
    def stanovi_vlasnika(self, upit):
        vlasnik_stanovi = {} 
        for stan in self.__stanovi:
            v = stan.vlasnik()   
            if v != None and v.ime_sadrzi(upit):   
                v_stanovi = vlasnik_stanovi.get(v.jmbg(), []) 
                v_stanovi.append(stan)         
                vlasnik_stanovi[v.jmbg()] = v_stanovi  
        return vlasnik_stanovi