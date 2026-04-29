from models import Warehouse, PhysicalProduct, DigitalProduct, OutOfStockError

def main(): 
    wh = Warehouse()

    
    pa = PhysicalProduct(1, "Laptop", 333.33, 1, 1.5, 5.0)
    pb = PhysicalProduct(2, "Subwoofer", 77.7, 2, 5.5, 15.0)
    pc = DigitalProduct(3, "Gladiator", 15.0, 999, "2027-01-01")
    pd = DigitalProduct(4, "Fifa 2027 Key", 55.5, 999, "2027-01-01") 


    wh.produkt_hinzufuegen(pa) 
    wh.produkt_hinzufuegen(pb) 
    wh.produkt_hinzufuegen(pc)
    wh.produkt_hinzufuegen(pd)

    try:
        wh.produkt_verkauf(2, 3)
    except OutOfStockError as e:
        print(f"Nicht genug da: {e}")

    
    print("\nProdukte mit wenig Bestand:")
    for produkt in wh.filter_inventar(): 
        print(f"- {produkt.name} (Nur noch {produkt.bestand} da!)")

    print("\nVerlauf:")
    for eintrag in wh.verlauf:
        print(eintrag)

if __name__ == "__main__":
    main()