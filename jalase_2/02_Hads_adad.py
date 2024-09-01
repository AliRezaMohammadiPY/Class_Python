"""
salam , toye in tamrin system yek adad beyn 1 ta 100 entekhab mikone
shoma bayad ba vared kardan adad oon adad ro peyda konid, system behetoon komak mikone ke bedoonin
adad az entekhabetoon bozorg tar ast ya koochek tar.
"""


import random
number = random.randint(1, 100)
while True:
    hads = input("Yek adad beyn 1 ta 100 : ")
    try:
        hads = int(hads)
    except ValueError:
        print("lotfan adad sahih vared konid!")
        continue
    if hads < 1 or hads > 100:
        print("Lotfan adad beyn 1 ta 100 begooid!")
        continue
    if hads == number:
        print("------------------------------------------------------\nTabrik migam dorost hads zadi :)")
        break
    elif hads >= number:
        print("adad koochek tar ast.")
    elif hads <= number:
        print("adad bozorg tar ast.")

print("khodahafez , Rooz khobi dashte bashi.")
