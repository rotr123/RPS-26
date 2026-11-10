#vaja1
# domaci=3
# gostje=1
# domaci, gostje= gostje, domaci
# skupaj=domaci+gostje
# print(f"{domaci}:{gostje}")
# print(f"skupaj: {skupaj}")

#vaja2
# zmin=4000
# min=zmin%60
# zur=zmin//60
# ura=zur%24
# dan=zur//24
# print(f"{dan} dni {ura} ur {min} min")

#vaja3
# št_dijakov=25
# cena_pice=9.50
# pic=9
# skupaj=85.5
# Na_dijaka=3.42
# pizza=št_dijakov//3
# if št_dijakov%3>0:
#     pizza+=1
# skupna_cena=pizza*cena_pice
# dijak_cena=skupna_cena/št_dijakov
# print(f"skupna cena za pizze je{skupna_cena}")
# print(f"{dijak_cena}")

#vaja4
# starost=int(input("Vpiši starost obiskovalca"))
# dan=str(input("Vpiši dan"))

# if starost <= 0:
#     print("starost je neveljavna")
# else:
#     if starost <= 5:
#         cena = 0
#     elif starost <= 17:
#         cena = 5
#     elif starost <= 64:
#         cena = 8
#     else:
#         cena = 6

#     if dan == "torek" and cena > 0:
#         cena -= 2

#     print("Cena:", cena, "EUR")

#vaja5
dni = int(input("Število dni: "))

c = 0

for i in range(1, dni + 1):
    if i % 7 != 0:
        c += i

    if c > 1000:
        print("Več kot 1000 EUR prvič na dan:", i)
        break

print("Prihranjeno:", c, "EUR")