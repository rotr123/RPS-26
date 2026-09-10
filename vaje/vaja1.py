x=5
y=15
z=-5

print(x-y)
print(x+y)
print(x*y)
print(x/y)

#decimalna (float) števila

x = 3.14
y = 10.012
print(0.5 + 0.5 == 1)
print(((0.1 + 0.2) - 0.3) < 0.00001)

#string - niz znakov
ime = "Luka"
print(ime)
print(len(ime))

st= "22"
print(st+st)
print(type(st))
print(st * 100)

print(int(st) + 100)

naslov = "kidriceva 55"

print(naslov.lower())
print(naslov.upper())
naslov=naslov.strip()
print(len(naslov))

ime = "luka colarič" #L. C.
ime= ime.upper() # LUKA COLARIČ
spltIme = ime.spilt()
print(type(spltIme))
print(spltIme)

ime=spltIme[0]
pri = spltIme[1] #altgr: f+g

print(ime, pri)
print(f"{ime}, {pri}")
