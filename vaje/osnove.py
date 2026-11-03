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
št_dijakov=25
cena_pice=9.50
pic=9
skupaj=85.5
Na_dijaka=3.42
pizza=št_dijakov//3
if št_dijakov%3>0:
    pizza+=1
skupna_cena=pizza*cena_pice
dijak_cena=skupna_cena/št_dijakov
print(f"skupna cena za pizze je{skupna_cena}")
print(f"{dijak_cena}")

#vaja4
a=int(input("Vpiši starost obiskovalca"))
b=str(input("Vpiši dan"))
