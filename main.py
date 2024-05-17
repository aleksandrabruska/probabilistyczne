with open("dane.txt") as file:
    data = file.read().split("\n")

lst = [float(i.replace(",",".")) for i in data]
print(lst)

def ord_mom1(lst):
    ex_1 = sum(lst)/len(lst)
    print("Moment zwykły rzędu 1: ", ex_1)

def ord_mom2(lst):
    ex_2 = sum([i**2 for i in lst])/len(lst)
    print("Moment zwykły rzędu 2: ",ex_2)

def cen_mom1(lst):
    mean = sum(lst)/len(lst)
    print("mean: ", mean)
    ex_3 = sum([(i - mean) for i in lst]) / len(lst)
    print("Moment centralny rzędu 1: ",ex_3)

def cen_mom2(lst):
    mean = sum(lst) / len(lst)
    ex_4 = sum([(i - mean)**2 for i in lst]) / len(lst)
    print("Moment centralny rzędu 2: ", ex_4)

def std(lst):
    ex_5 = cen_mom2(lst)**(0.5)
    print("Odchylenie standardowe: ", ex_5)

def avg_dev(lst):
    mean = sum(lst) / len(lst)
    ex_6 = sum([abs(i - mean) for i in lst]) / len(lst)
    print("Odchylenie przeciętne: ", ex_6)