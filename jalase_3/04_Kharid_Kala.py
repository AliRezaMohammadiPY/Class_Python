"""
salam, tooye in tamrin shoma bayad 'nam kala' va 'hazine kala' ro bedid (tekrari ham mitoone bashe)
barname miad gheymat haro hesab mikone, boodje shoma ro migire va mige : shoma mitoonid pardakht konid
ya mige nemtoonid pardakht konid.
"""


print("-------------------------------------\nagar benvisid 'next' be marhale bad "
      "miravid.\n-------------------------------------")

name_vasile = {}


def kharid_kala():
    while True:
        try:
            kala = str(input("Kala ye Morede nazar khod ra vared konid : "))
            if kala.lower() == "next":
                break
            hazine = input("hazine Kala chaghadr ast? ")
            hazine = int(hazine)
        except ValueError:
            print("adad sahih vared kon!")
            continue

        if kala in name_vasile.keys():
            hazine_1 = name_vasile.get(kala) + hazine
            name_vasile.update({kala: hazine_1})
        else:
            name_vasile.update({kala: hazine})
    return name_vasile
list_Kala = kharid_kala()
def majmoo_hazine():
    majmoo = 0
    for numbers in list_Kala.values():
        majmoo += numbers
    return majmoo
jam_kala = majmoo_hazine()
def boodje():
    while True:
        boodje_karbar = input("Boodje shoma cheghadr ast?")
        try:
            boodje_karbar = int(boodje_karbar)
            break
        except ValueError:
            print("adad sahih vared kon!, dobare emtehan kon.")
            continue
    baghi_mande = boodje_karbar - jam_kala
    if 0 > baghi_mande:
        print(f"--------------------\nHazine kala ha : {jam_kala}")
        print("Hazine kala ha Bishtar az Boodje shoma hast !")
    else:
        print("shoma mitavanid pardakht konid. :)")
        print(f"--------------------\nHazine Kala ha ({jam_kala}) ast ,boodje shoma ({boodje_karbar}) ast ")
        print(f"Hazine Baghi mandeh : {baghi_mande}")
    return
boodje()
