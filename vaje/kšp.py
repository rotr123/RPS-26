def igra():
    print("Dobrodošli v igri KŠP!")
    print("Izberite svojo potezo: kamen, škarje ali papir.")
    
    
    uporabnik_poteza = input("Vaša poteza: ").lower()
    
    
    import random
    racunalnik_poteza = random.choice(["kamen", "škarje", "papir"])
    
    print(f"Računalnik je izbral: {racunalnik_poteza}")
    

    if uporabnik_poteza == racunalnik_poteza:
        print("Neodločeno!")
    elif (uporabnik_poteza == "kamen" and racunalnik_poteza == "škarje") or \
         (uporabnik_poteza == "škarje" and racunalnik_poteza == "papir") or \
         (uporabnik_poteza == "papir" and racunalnik_poteza == "kamen"):
        print("Zmagali ste!")
    else:
        print("Zmagal je računalnik!")

def main():
    while True:
        igra()
        ponovno = input("Ali želite igrati še enkrat? (da/ne): ").lower()
        if ponovno != "da":
            print("Hvala za igro! Nasvidenje!")
            break

if __name__ == "__main__":
    main()