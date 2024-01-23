
def beker():
    modszer:str=str(input("Színkeverési módszer: "))
    kod:str=str(input("Kérem a kódot: "))
    if modszer=="HEX":
        if len(kod)==6:
            print("megfelelő hossz")
        else:
            print("nem megfelelő hossz")
    elif modszer=="RGB":
        if 5<len(kod) or 11>len(kod):
            print("megfelelő hossz")
        else:
            print("nem megfelelő hossz")
    elif modszer=="HSL":
        if 7<len(kod) or 13>len(kod):
            print("megfelelő hossz")
        else:
            print("nem megfelelő hossz")