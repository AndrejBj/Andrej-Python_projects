import Osoba as f
 
z = f.Zaposleni('Aca', 'Vukic', '12153', 95000, '3a', '4218-589')
s = f.Student('Mitar', 'Miric', '12131', '119/17', 'MTI')
print(isinstance(s, f.Student), isinstance(s, f.Osoba))
print(isinstance(z, f.Student), isinstance(z, f.Osoba))
 
z.predstavi_se()
s.predstavi_se()
 
print(z)
print(s)