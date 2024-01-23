from Auto import Auto
def beolvas():
    fajl=open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    kocsi=[]
    for i in range(0, len(nyers_lista), 1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split(":")
        nev=sor_tag[0]
        gyd=int(sor_tag[1])
        auto=Auto(nev, int(gyd))
        kocsi.append(auto)
    return kocsi

def kor(auto):
    eves=2024-auto.gyd
    return eves

def kiir(auto, eves):
    fajl=open("ki.txt", "w", encoding="utf-8")
    fajl.write(f"\t{auto.nev} - {eves}")
    fajl.close()

def flotta(kocsi):
    hany=len(kocsi)
    return hany

def ertekes(kocsi):
    lg_index=0
    for i in range(0, len(kocsi),1):
        if kocsi[lg_index].gyd>kocsi[i].gyd:
            lg_index=i
    return lg_index