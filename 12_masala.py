son = input("Son kiriting>>> ")
try:
    butun_s = int(son)
    if butun_s>0:
        if butun_s%2==0:
            print(f"{son} butun son juft son musbat son")
        else:
            print(f"{son} butun son toq son musbat son")
    else:
        print(f"{son} butun son  manfiy son")


            
except:
    kasr_s = float(son)
    if kasr_s>0:
        if kasr_s%2==0.0:
            print(f"{son} kasr son juft son musbat son")
        else:
            print(f"{son} kasr son toq son musbat son")
    else:
        print(f"{son} kasr son  manfiy son")