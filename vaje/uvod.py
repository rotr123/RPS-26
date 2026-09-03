
def hello():
    oddelek = input("kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
        print(f"Hello {oddelek}<3")
    else:
        print(f"Hello {oddelek}")

if __name__ == "__main__":
    hello()