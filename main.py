import oszthato
import autom
import szin

"""
print("Első feladat:")
szin.beker()


print("Masodik feladat:")
lista=oszthato.szamsorozat()
print(f"A lista elemei:\n \t{lista}")
szamlalo=oszthato.hettelOszthato(lista)
print(f"\nA listában {szamlalo} darab héttel osztható szám van.")"""


kocsi=autom.beolvas()
print("III/Kor:")
eves=autom.kor(kocsi[4])
print(f"\t{kocsi[4].nev} - {eves}")

print("III/Flotta:")
hany=autom.flotta(kocsi)
print(f"\tAutók száma: {hany}")

print("III/Ertekes:")
lg_index=autom.ertekes(kocsi)
print(f"\tA legöregebb autó: {kocsi[lg_index].nev}: {kocsi[lg_index].gyd}")

autom.kiir(kocsi[4], eves)
