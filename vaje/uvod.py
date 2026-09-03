
def hello():
    oddelek = input("kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
        print(f"Hello {oddelek}<3")
    else:
        print(f"Hello {oddelek}")

def poštevanka():
    x = int(input("Izberi si številko"))
    št = 1
    while št <= 10:
        print(f"{x} * {št} = {x * št}")
        št += 1

if __name__ == "__main__":
    # hello()
    poštevanka()
