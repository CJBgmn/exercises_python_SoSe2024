def teilbar (x,y):
    if y==0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    elif x == y:
        print("x und y sind gleich")
    elif x % y == 0:
        print(f"{x} ist durch {y} teilbar")
    else:
        print(f"{x} ist nicht durch {y} teilbar")
        
teilbar(5,0)
