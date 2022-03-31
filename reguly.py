import math

# ----------------------SŁOWNIK_REGULY----------------------
# kluczem jest zestawienie etykiet dla P40, HW, sigma, HHmax
# np.  0212 -> P40 - low
#             HW - high
#             sigma - medium
#             HHmax - high
slownik_reguly = {  
    '0202' : ['notLy',1],
    '0201' : ['notLy',2],
    '0200' : ['notLy',3],
    '0212' : ['notLy',4],
    '0211' : ['notLy',5],
    '0210' : ['mayLy',6],
    '0222' : ['notLy',7],
    '0221' : ['mayLy',8],
    '0220' : ['mayLy',9],
    '0102' : ['notLy',10],
    '0101' : ['notLy',11],
    '0100' : ['mayLy',12],
    '0112' : ['notLy',13],
    '0111' : ['mayLy',14],
    '0110' : ['mayLy',15],
    '0122' : ['mayLy',16],
    '0121' : ['mayLy',17],
    '0120' : ['mayLy',18],
    '0002' : ['notLy',19],
    '0001' : ['mayLy',20],
    '0000' : ['mayLy',21],
    '0012' : ['mayLy',22],
    '0011' : ['mayLy',23],
    '0010' : ['mayLy',24],
    '0022' : ['mayLy',25],
    '0021' : ['mayLy',26],
    '0020' : ['isLy',27],
    '1202' : ['notLy',28],
    '1201' : ['notLy',29],
    '1200' : ['mayLy',30],
    '1212' : ['notLy',31],
    '1211' : ['mayLy',32],
    '1210' : ['mayLy',33],
    '1222' : ['mayLy',34],
    '1221' : ['mayLy',35],
    '1220' : ['mayLy',36],
    '1102' : ['notLy',37],
    '1101' : ['mayLy',38],
    '1100' : ['mayLy',39],
    '1112' : ['mayLy',40],
    '1111' : ['mayLy',41],
    '1110' : ['mayLy',42],
    '1122' : ['mayLy',43],
    '1121' : ['mayLy',44],
    '1120' : ['isLy',45],
    '1002' : ['mayLy',46],
    '1001' : ['mayLy',47],
    '1000' : ['mayLy',48],
    '1012' : ['mayLy',49],
    '1011' : ['mayLy',50],
    '1010' : ['isLy',51],
    '1022' : ['mayLy',52],
    '1021' : ['isLy',53],
    '1020' : ['isLy',54],
    '2202' : ['notLy',55],
    '2201' : ['mayLy',56],
    '2200' : ['mayLy',57],
    '2212' : ['mayLy',58],
    '2211' : ['mayLy',59],
    '2210' : ['mayLy',60],
    '2222' : ['mayLy',61],
    '2221' : ['mayLy',62],
    '2220' : ['isLy',63],
    '2102' : ['mayLy',64],
    '2101' : ['mayLy',65],
    '2100' : ['mayLy',66],
    '2112' : ['mayLy',67],
    '2111' : ['mayLy',68],
    '2110' : ['isLy',69],
    '2122' : ['mayLy',70],
    '2121' : ['isLy',71],
    '2120' : ['isLy',72],
    '2002' : ['mayLy',73],
    '2001' : ['mayLy',74],
    '2000' : ['isLy',75],
    '2012' : ['mayLy',76],
    '2011' : ['isLy',77],
    '2010' : ['isLy',78],
    '2022' : ['isLy',79],
    '2021' : ['isLy',80],
    '2020' : ['isLy',81] }

slownik_nowe_reguly = {
    '020x' : ['notLy',1],
    '02x2' : ['notLy',2],
    '0x02' : ['notLy',3],
    'x202' : ['notLy',4],
    '0x01' : ['notLy',5],
    '0211' : ['notLy',6],
    '0112' : ['notLy',7],
    '1201' : ['notLy',8],
    '1212' : ['notLy',9],
    '1102' : ['notLy',10],
    '11x1' : ['mayLy',11],
    '001x' : ['mayLy',12],
    '100x' : ['mayLy',13],
    '221x' : ['mayLy',14],
    '012x' : ['mayLy',15],
    'x221' : ['mayLy',16],
    '1x22' : ['mayLy',17],
    '12x0' : ['mayLy',18],
    '21x2' : ['mayLy',19],
    '2002' : ['mayLy',20],
    '0022' : ['mayLy',21],
    '111x' : ['mayLy',22],
    'x012' : ['mayLy',23],
    'x210' : ['mayLy',24],
    '01x0' : ['mayLy',25],
    '2200' : ['mayLy',26],
    '00x1' : ['mayLy',27],
    'x111' : ['mayLy',28],
    '0000' : ['mayLy',29],
    '2222' : ['mayLy',30],
    '2x01' : ['mayLy',31],
    '0220' : ['mayLy',32],
    'x100' : ['mayLy',33],
    '1x11' : ['mayLy',34],
    '202x' : ['isLy',35],
    '2110' : ['isLy',36],
    '20x0' : ['isLy',37],
    '2x20' : ['isLy',38],
    'x020' : ['isLy',39],
    '2011' : ['isLy',40],
    '2121' : ['isLy',41],
    '1010' : ['isLy',42],
    '1120' : ['isLy',43],
    '1021' : ['isLy',44]    
    }
# słowniki zawierajace przynaleznosci do danej etykiety,
# wartosci wyznaczane sa na bazie slownika regul
isLy = {}
mayLy = {}
notLy = {}

isLy_pom = {}
mayLy_pom = {}
notLy_pom = {}

isLy_nowe = {}
mayLy_nowe = {}
notLy_nowe = {}

def agregacja_A(klucz, P40, HW, sigma, HHmax):
    minimum = [min(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),min(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
    maximum = [max(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),max(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
    mean = [(P40[int(klucz[0])][0] + HW[int(klucz[1])][0] + sigma[int(klucz[2])][0] + HHmax[int(klucz[3])][0]) / 4 , (P40[int(klucz[0])][1]+ HW[int(klucz[1])][1]+ sigma[int(klucz[2])][1]+ HHmax[int(klucz[3])][1]) /4]
    g_mean = [pow(P40[int(klucz[0])][0] * HW[int(klucz[1])][0] * sigma[int(klucz[2])][0] * HHmax[int(klucz[3])][0] , 1/4), pow(P40[int(klucz[0])][1] * HW[int(klucz[1])][1] * sigma[int(klucz[2])][1] * HHmax[int(klucz[3])][1] , 1/4)]
    sum_sq_down = (pow(P40[int(klucz[0])][0], 2) + pow(HW[int(klucz[1])][0], 2) + pow(sigma[int(klucz[2])][0], 2) + pow(HHmax[int(klucz[3])][0], 2) )  # zmienna pomocnicza
    sum_sq_up = (pow(P40[int(klucz[0])][1], 2) + pow(HW[int(klucz[1])][1], 2) + pow(sigma[int(klucz[2])][1], 2) + pow(HHmax[int(klucz[3])][1], 2) )  # zmienna pomocnicza
    sq_mean = [pow(sum_sq_down / 4 , 1/2), pow(sum_sq_up / 4 , 1/2)]

    return minimum

def agregacja_A_nowe(klucz, P40, HW, sigma, HHmax):
    if klucz[0] == 'x':
        minimum = [min(HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),min(HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        maximum = [max(HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),max(HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        mean = [(HW[int(klucz[1])][0] + sigma[int(klucz[2])][0] + HHmax[int(klucz[3])][0]) / 3 , (HW[int(klucz[1])][1] + sigma[int(klucz[2])][1] + HHmax[int(klucz[3])][1]) /3]
        g_mean = [pow(HW[int(klucz[1])][0] * sigma[int(klucz[2])][0] * HHmax[int(klucz[3])][0] , 1/3), pow(HW[int(klucz[1])][1] * sigma[int(klucz[2])][1] * HHmax[int(klucz[3])][1] , 1/3)]
        sum_sq_down = (pow(HW[int(klucz[1])][0], 2) + pow(sigma[int(klucz[2])][0], 2) + pow(HHmax[int(klucz[3])][0], 2) )  # zmienna pomocnicza
        sum_sq_up = (pow(HW[int(klucz[1])][1], 2) + pow(sigma[int(klucz[2])][1], 2) + pow(HHmax[int(klucz[3])][1], 2) )  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 3 , 1/2), pow(sum_sq_up / 3 , 1/2)]

    elif klucz[1] == 'x':
        minimum = [min(P40[int(klucz[0])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),min(P40[int(klucz[0])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        maximum = [max(P40[int(klucz[0])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),max(P40[int(klucz[0])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        mean = [(P40[int(klucz[0])][0] + sigma[int(klucz[2])][0] + HHmax[int(klucz[3])][0]) / 3 , (P40[int(klucz[0])][1] + sigma[int(klucz[2])][1] + HHmax[int(klucz[3])][1]) /3]
        g_mean = [pow(P40[int(klucz[0])][0] * sigma[int(klucz[2])][0] * HHmax[int(klucz[3])][0] , 1/3), pow(P40[int(klucz[0])][1] * sigma[int(klucz[2])][1] * HHmax[int(klucz[3])][1] , 1/3)]
        sum_sq_down = (pow(P40[int(klucz[0])][0], 2) + pow(sigma[int(klucz[2])][0], 2) + pow(HHmax[int(klucz[3])][0], 2) )  # zmienna pomocnicza
        sum_sq_up = (pow(P40[int(klucz[0])][1], 2) + pow(sigma[int(klucz[2])][1], 2) + pow(HHmax[int(klucz[3])][1], 2) )  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 3 , 1/2), pow(sum_sq_up / 3 , 1/2)]

    elif klucz[2] == 'x':
        minimum = [min(P40[int(klucz[0])][0], HW[int(klucz[1])][0], HHmax[int(klucz[3])][0]),min(P40[int(klucz[0])][1], HW[int(klucz[1])][1], HHmax[int(klucz[3])][1])]
        maximum = [max(P40[int(klucz[0])][0], HW[int(klucz[1])][0], HHmax[int(klucz[3])][0]),max(P40[int(klucz[0])][1], HW[int(klucz[1])][1], HHmax[int(klucz[3])][1])]
        mean = [(P40[int(klucz[0])][0] + HW[int(klucz[1])][0] + HHmax[int(klucz[3])][0]) / 3 , (P40[int(klucz[0])][1] + HW[int(klucz[1])][1] + HHmax[int(klucz[3])][1]) /3]
        g_mean = [pow(P40[int(klucz[0])][0] * HW[int(klucz[1])][0] * HHmax[int(klucz[3])][0] , 1/3), pow(P40[int(klucz[0])][1] * HW[int(klucz[1])][1] * HHmax[int(klucz[3])][1] , 1/3)]
        sum_sq_down = (pow(P40[int(klucz[0])][0], 2) + pow(HW[int(klucz[1])][0], 2) + pow(HHmax[int(klucz[3])][0], 2) )  # zmienna pomocnicza
        sum_sq_up = (pow(P40[int(klucz[0])][1], 2) + pow(HW[int(klucz[1])][1], 2) + pow(HHmax[int(klucz[3])][1], 2) )  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 3 , 1/2), pow(sum_sq_up / 3 , 1/2)]

    elif klucz[3] == 'x':
        minimum = [min(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0]),min(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1])]
        maximum = [max(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0]),max(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1])]
        mean = [(P40[int(klucz[0])][0] + HW[int(klucz[1])][0] + sigma[int(klucz[2])][0]) / 3 , (P40[int(klucz[0])][1] + HW[int(klucz[1])][1] + sigma[int(klucz[2])][1]) /3]
        g_mean = [pow(P40[int(klucz[0])][0] * HW[int(klucz[1])][0] * sigma[int(klucz[2])][0] , 1/3), pow(P40[int(klucz[0])][1] * HW[int(klucz[1])][1] * sigma[int(klucz[2])][1] , 1/3)]
        sum_sq_down = (pow(P40[int(klucz[0])][0], 2) + pow(HW[int(klucz[1])][0], 2) + pow(sigma[int(klucz[2])][0], 2))  # zmienna pomocnicza
        sum_sq_up = (pow(P40[int(klucz[0])][1], 2) + pow(HW[int(klucz[1])][1], 2) + pow(sigma[int(klucz[2])][1], 2))  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 3 , 1/2), pow(sum_sq_up / 3 , 1/2)]

    else:
        minimum = [min(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),min(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        maximum = [max(P40[int(klucz[0])][0], HW[int(klucz[1])][0], sigma[int(klucz[2])][0], HHmax[int(klucz[3])][0]),max(P40[int(klucz[0])][1], HW[int(klucz[1])][1], sigma[int(klucz[2])][1], HHmax[int(klucz[3])][1])]
        mean = [(P40[int(klucz[0])][0] + HW[int(klucz[1])][0] + sigma[int(klucz[2])][0] + HHmax[int(klucz[3])][0]) / 4 , (P40[int(klucz[0])][1] + HW[int(klucz[1])][1] + sigma[int(klucz[2])][1] + HHmax[int(klucz[3])][1]) /4]
        g_mean = [pow(P40[int(klucz[0])][0] * HW[int(klucz[1])][0] * sigma[int(klucz[2])][0] * HHmax[int(klucz[3])][0] , 1/4), pow(P40[int(klucz[0])][1] * HW[int(klucz[1])][1] * sigma[int(klucz[2])][1] * HHmax[int(klucz[3])][1] , 1/4)]
        sum_sq_down = (pow(P40[int(klucz[0])][0], 2) + pow(HW[int(klucz[1])][0], 2) + pow(sigma[int(klucz[2])][0], 2) + pow(HHmax[int(klucz[3])][0], 2) )  # zmienna pomocnicza
        sum_sq_up = (pow(P40[int(klucz[0])][1], 2) + pow(HW[int(klucz[1])][1], 2) + pow(sigma[int(klucz[2])][1], 2) + pow(HHmax[int(klucz[3])][1], 2) )  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 4 , 1/2), pow(sum_sq_up / 4 , 1/2)]

    return sq_mean

# x0 jest oznaczeniem gdy jest 0 to używam: sigma(al,0)
#                     gdy jest 1 to używam: sigma(1,al)
def agregacja_K_sigma(x0,al):
    if x0 == 1:
        minimum = [min([0,al[0]]), min([0,al[1]])]
        maximum = [max([0,al[0]]), max([0,al[1]])]
        mean = [(0 + al[0]) / 2 , (0 + al[1]) /2]
        g_mean = [pow(0 * al[0] , 1/2), pow(0 * al[1] , 1/2)]
        sum_sq_down = pow(0, 2) + pow(al[0], 2)  # zmienna pomocnicza
        sum_sq_up = pow(0, 2) + pow(al[1], 2)  # zmienna pomocnicza  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 2 , 1/2), pow(sum_sq_up / 2 , 1/2)]
    
    if x0 == 0:
        minimum = [min([1-al[1], 0]), min([1-al[0],0])]
        maximum = [max([1-al[1], 0]), max([1-al[0],0])]
        mean = [((1-al[1]) + 0) / 2 , ((1-al[0]) + 0) /2]
        g_mean = [pow(0 * (1-al[0]) , 1/2), pow(0 * (1-al[1]) , 1/2)]
        sum_sq_down = pow(0, 2) + pow(1-al[0], 2)  # zmienna pomocnicza
        sum_sq_up = pow(0, 2) + pow(1-al[1], 2)  # zmienna pomocnicza  # zmienna pomocnicza
        sq_mean = [pow(sum_sq_down / 2 , 1/2), pow(sum_sq_up / 2 , 1/2)]

    return maximum 

def operator_N(z):
    z=[z[0][0],z[0][1]]
    return [1-z[1], 1-z[0]]

def operator_D(z1,z2):
    przedzial1 = abs( (z1[0]+z1[1])/2 - (z2[0]-z2[1])/2)
    przedzial2 = przedzial1 + (((z1[1]-z1[0]) + (z2[1]-z2[0] ))/2)
    return [przedzial1, przedzial2]

def agregacja_B(A, K): 
    minimum = [min(A[0],K[0]), min(A[1],K[1])]
    maximum = [max(A[0],K[0]), max(A[1],K[1])]
    mean = [(A[0]+K[0]) / 2 , (A[1]+K[1]) /2]
    g_mean = [pow(A[0] * K[0], 1/2) , pow(A[1] * K[1], 1/2) ]
    sum_sq_down = pow(A[0], 2) + pow(K[0], 2)   # zmienna pomocnicza
    sum_sq_up = pow(A[1], 2) + pow(K[1], 2)  # zmienna pomocnicza
    sq_mean = [pow(sum_sq_down / 2 , 1/2), pow(sum_sq_up / 2 , 1/2)]

    return maximum  

def min_przedzialy(x1,x2):
    return [min(x1[0],x2[0]),min(x1[1],x2[1])]

#sprawdza czy mianownik jest != 0
def mianownik_0(licznik,mianownik):
    if mianownik[0] == 0:
        return [1, licznik[1]/mianownik[1]]
    elif mianownik[1] == 0:
        return [licznik[0]/mianownik[0], 1]
    else:
        return [licznik[0]/mianownik[0], licznik[1]/mianownik[1]]

def operator_K(klucz, P40, HW, sigma, HHmax):

    licznik = operator_D(agregacja_K_sigma(1,P40[int(klucz[0])]), agregacja_K_sigma(0,P40[int(klucz[0])]))
    mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,P40[int(klucz[0])]),agregacja_K_sigma(0,P40[int(klucz[0])]))])
    wynik1 = mianownik_0(licznik,mianownik)
       
    licznik = operator_D(agregacja_K_sigma(1,HW[int(klucz[1])]), agregacja_K_sigma(0,HW[int(klucz[1])]))
    mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HW[int(klucz[1])]),agregacja_K_sigma(0,HW[int(klucz[1])]))])
    wynik2 = mianownik_0(licznik,mianownik)
   
    licznik = operator_D(agregacja_K_sigma(1,sigma[int(klucz[2])]),  agregacja_K_sigma(0,sigma[int(klucz[2])]))
    mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,sigma[int(klucz[2])]),agregacja_K_sigma(0,sigma[int(klucz[2])]))])
    wynik3 = mianownik_0(licznik,mianownik)
   
    licznik = operator_D(agregacja_K_sigma(1,HHmax[int(klucz[3])]),  agregacja_K_sigma(0,HHmax[int(klucz[3])]))
    mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HHmax[int(klucz[3])]),agregacja_K_sigma(0,HHmax[int(klucz[3])]))])
    wynik4 = mianownik_0(licznik,mianownik)
        
    suma = [(wynik1[0]+wynik2[0]+wynik3[0]+wynik4[0])/4, (wynik1[1]+wynik2[1]+wynik3[1]+wynik4[1])/4]
    return suma

def operator_K_nowe(klucz, P40, HW, sigma, HHmax):
    if klucz[0] == 'x':   
        licznik = operator_D(agregacja_K_sigma(1,HW[int(klucz[1])]),  agregacja_K_sigma(0,HW[int(klucz[1])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HW[int(klucz[1])]),agregacja_K_sigma(0,HW[int(klucz[1])]))])
        wynik2 = mianownik_0(licznik,mianownik)
     
        licznik = operator_D(agregacja_K_sigma(1,sigma[int(klucz[2])]),  agregacja_K_sigma(0,sigma[int(klucz[2])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,sigma[int(klucz[2])]),agregacja_K_sigma(0,sigma[int(klucz[2])]))])
        wynik3 = mianownik_0(licznik,mianownik)
    
        licznik = operator_D(agregacja_K_sigma(1,HHmax[int(klucz[3])]),  agregacja_K_sigma(0,HHmax[int(klucz[3])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HHmax[int(klucz[3])]),agregacja_K_sigma(0,HHmax[int(klucz[3])]))])
        wynik4 = mianownik_0(licznik,mianownik)

        suma = [(wynik2[0]+wynik3[0]+wynik4[0])/3, (wynik2[1]+wynik3[1]+wynik4[1])/3]

    elif klucz[1] == 'x':
        licznik = operator_D(agregacja_K_sigma(1,P40[int(klucz[0])]),  agregacja_K_sigma(0,P40[int(klucz[0])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,P40[int(klucz[0])]),agregacja_K_sigma(0,P40[int(klucz[0])]))])
        wynik1 = mianownik_0(licznik,mianownik)

        licznik = operator_D(agregacja_K_sigma(1,sigma[int(klucz[2])]),  agregacja_K_sigma(0,sigma[int(klucz[2])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,sigma[int(klucz[2])]),agregacja_K_sigma(0,sigma[int(klucz[2])]))])
        wynik3 = mianownik_0(licznik,mianownik)
    
        licznik = operator_D(agregacja_K_sigma(1,HHmax[int(klucz[3])]),  agregacja_K_sigma(0,HHmax[int(klucz[3])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HHmax[int(klucz[3])]),agregacja_K_sigma(0,HHmax[int(klucz[3])]))])
        wynik4 = mianownik_0(licznik,mianownik)

        suma = [(wynik1[0]+wynik3[0]+wynik4[0])/3, (wynik1[1]+wynik3[1]+wynik4[1])/3]

    elif klucz[2] == 'x':
        licznik = operator_D(agregacja_K_sigma(1,P40[int(klucz[0])]),  agregacja_K_sigma(0,P40[int(klucz[0])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,P40[int(klucz[0])]),agregacja_K_sigma(0,P40[int(klucz[0])]))])
        wynik1 = mianownik_0(licznik,mianownik)

        licznik = operator_D(agregacja_K_sigma(1,HW[int(klucz[1])]),  agregacja_K_sigma(0,HW[int(klucz[1])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HW[int(klucz[1])]),agregacja_K_sigma(0,HW[int(klucz[1])]))])
        wynik2 = mianownik_0(licznik,mianownik)
     
        licznik = operator_D(agregacja_K_sigma(1,HHmax[int(klucz[3])]),  agregacja_K_sigma(0,HHmax[int(klucz[3])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HHmax[int(klucz[3])]),agregacja_K_sigma(0,HHmax[int(klucz[3])]))])
        wynik4 = mianownik_0(licznik,mianownik)

        suma = [(wynik1[0]+wynik2[0]+wynik4[0])/3, (wynik1[1]+wynik2[1]+wynik4[1])/3]

    elif klucz[3] == 'x':
        licznik = operator_D(agregacja_K_sigma(1,P40[int(klucz[0])]),  agregacja_K_sigma(0,P40[int(klucz[0])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,P40[int(klucz[0])]),agregacja_K_sigma(0,P40[int(klucz[0])]))])
        wynik1 = mianownik_0(licznik,mianownik)
    
        licznik = operator_D(agregacja_K_sigma(1,HW[int(klucz[1])]),  agregacja_K_sigma(0,HW[int(klucz[1])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,HW[int(klucz[1])]),agregacja_K_sigma(0,HW[int(klucz[1])]))])
        wynik2 = mianownik_0(licznik,mianownik)
     
        licznik = operator_D(agregacja_K_sigma(1,sigma[int(klucz[2])]),  agregacja_K_sigma(0,sigma[int(klucz[2])]))
        mianownik = operator_N([min_przedzialy(agregacja_K_sigma(1,sigma[int(klucz[2])]),agregacja_K_sigma(0,sigma[int(klucz[2])]))])
        wynik3 = mianownik_0(licznik,mianownik)
    
        suma = [(wynik1[0]+wynik2[0]+wynik3[0])/3, (wynik1[1]+wynik2[1]+wynik3[1])/3]

    else:
        suma = operator_K(klucz, P40, HW, sigma, HHmax)
        
    return suma

def zamien_na_przedzial(x):
    for i in range(3):
         if x[i] is not None:
             x[i] = [x[i],x[i]]
         else:
             x[i] = [0,1]
    #print("\nprintuje x z funkcji zamien_na_przedzial: ",x,"\n")
    return x

def przynal_do_pozycji(P40, HW, sigma, HHmax):
    P40 = zamien_na_przedzial(P40)
    HW = zamien_na_przedzial(HW)
    sigma = zamien_na_przedzial(sigma)
    HHmax = zamien_na_przedzial(HHmax)
    for iP40 in range(3):
        for iHW in range(3):
            for isigma in range(3):
                for iHHmax in range(3):
                    klucz = str(iP40) + str(iHW) + str(isigma) + str(iHHmax)
                    wartosc_slownik = slownik_reguly.get(klucz)
                    #print("klucz: ",klucz)
                    #print("wartosc slownik: ",wartosc_slownik)
                    nr_reguly = wartosc_slownik[1]
                    pozycja = wartosc_slownik[0]
                    
                    if pozycja == 'isLy':
                        wartosc_agreg_A = agregacja_A(klucz,P40, HW, sigma, HHmax)
                        wartosc_op_K = operator_K(klucz,P40, HW, sigma, HHmax)
                        wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
                        isLy[nr_reguly] = wartosc_agreg_B                            #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'mayLy':   
                        wartosc_agreg_A = agregacja_A(klucz,P40, HW, sigma, HHmax)
                        wartosc_op_K = operator_K(klucz,P40, HW, sigma, HHmax)
                        wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
                        mayLy[nr_reguly] = wartosc_agreg_B                           #wrzuc aktualne wartosci tablic parametrow
                    elif pozycja == 'notLy': 
                        wartosc_agreg_A = agregacja_A(klucz,P40, HW, sigma, HHmax)
                        wartosc_op_K = operator_K(klucz,P40, HW, sigma, HHmax)
                        wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
                        notLy[nr_reguly] = wartosc_agreg_B                           #wrzuc aktualne wartosci tablic parametrow
  
def przynal_do_poz_nowe(P40, HW, sigma, HHmax):
    P40 = zamien_na_przedzial(P40)
    HW = zamien_na_przedzial(HW)
    sigma = zamien_na_przedzial(sigma)
    HHmax = zamien_na_przedzial(HHmax)

    for k in slownik_nowe_reguly.keys():
        wartosc_slownik = slownik_nowe_reguly.get(k)
        nr_reguly = wartosc_slownik[1]
        pozycja = wartosc_slownik[0]
        if pozycja == 'isLy':
            wartosc_agreg_A = agregacja_A_nowe(k,P40, HW, sigma, HHmax)
            wartosc_op_K = operator_K_nowe(k,P40, HW, sigma, HHmax)
            wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
            isLy_nowe[nr_reguly] = wartosc_agreg_B                            #wrzuc aktualne wartosci tablic parametrow
        elif pozycja == 'mayLy':                        
            wartosc_agreg_A = agregacja_A_nowe(k,P40, HW, sigma, HHmax)
            wartosc_op_K = operator_K_nowe(k,P40, HW, sigma, HHmax)
            wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
            mayLy_nowe[nr_reguly] = wartosc_agreg_B                            #wrzuc aktualne wartosci tablic parametrow
        elif pozycja == 'notLy':                       
            wartosc_agreg_A = agregacja_A_nowe(k,P40, HW, sigma, HHmax)
            wartosc_op_K = operator_K_nowe(k,P40, HW, sigma, HHmax)
            wartosc_agreg_B = agregacja_B(wartosc_agreg_A, wartosc_op_K)
            notLy_nowe[nr_reguly] = wartosc_agreg_B                            #wrzuc aktualne wartosci tablic parametrow
                        
def defuzyfikacja():
    
    list_isLy_values = list(isLy.values())
    max_isLy0 = list_isLy_values[0][0]
    max_isLy1 = list_isLy_values[0][1]
        
    for i in list_isLy_values:
        max_isLy0 = list_isLy_values[0][0]
        max_isLy1 = list_isLy_values[0][1]
        if max_isLy0 < i[0]:
            max_isLy0 = i[0]
        if max_isLy1 < i[1]:
            max_isLy1 = i[1]


    list_mayLy_values = list(mayLy.values())
    max_mayLy0 = list_mayLy_values[0][0]
    max_mayLy1 = list_mayLy_values[0][1]

    for i in list_mayLy_values:
        max_mayLy0 = list_mayLy_values[0][0]
        max_mayLy1 = list_mayLy_values[0][1]
        if max_mayLy0 < i[0]:
            max_mayLy0 = i[0]
        if max_mayLy1 < i[1]:
            max_mayLy1 = i[1]

 
    list_notLy_values = list(notLy.values())
    max_notLy0 = list_notLy_values[0][0]
    max_notLy1 = list_notLy_values[0][1]

    for i in list_notLy_values:
        max_notLy0 = list_notLy_values[0][0]
        max_notLy1 = list_notLy_values[0][1]
        if max_notLy0 < i[0]:
            max_notLy0 = i[0]
        if max_notLy1 < i[1]:
            max_notLy1 = i[1]


    if (max_isLy0 + max_mayLy0 + max_notLy0) == 0:
        wynik0 = 1
        wynik1 = 1
    else:
        wynik0 = ((0.11 * max_isLy0) + (0.5 * max_mayLy0) + (0.885 * max_notLy0)) / (max_isLy0 + max_mayLy0 + max_notLy0)
        wynik1 = ((0.11 * max_isLy1) + (0.5 * max_mayLy1) + (0.885 * max_notLy1)) / (max_isLy1 + max_mayLy1 + max_notLy1)
    
    #print("wynik: ",wynik0, ", ",wynik1)

    if wynik0 >= 0.5 and wynik1 >= 0.5:
        return 'notLy'
    else:
        return [wynik0,wynik1]

i = 0

def defuzyfikacja_nowe():

    list_isLy_values = list(isLy_nowe.values())
    max_isLy0 = list_isLy_values[0][0]
    max_isLy1 = list_isLy_values[0][1]
        
    for i in list_isLy_values:
        max_isLy0 = list_isLy_values[0][0]
        max_isLy1 = list_isLy_values[0][1]
        if max_isLy0 < i[0]:
            max_isLy0 = i[0]
        if max_isLy1 < i[1]:
            max_isLy1 = i[1]
    

    list_mayLy_values = list(mayLy_nowe.values())
    max_mayLy0 = list_mayLy_values[0][0]
    max_mayLy1 = list_mayLy_values[0][1]

    for i in list_mayLy_values:
        max_mayLy0 = list_mayLy_values[0][0]
        max_mayLy1 = list_mayLy_values[0][1]
        if max_mayLy0 < i[0]:
            max_mayLy0 = i[0]
        if max_mayLy1 < i[1]:
            max_mayLy1 = i[1]
 

    list_notLy_values = list(notLy_nowe.values())
    max_notLy0 = list_notLy_values[0][0]
    max_notLy1 = list_notLy_values[0][1]

    for i in list_notLy_values:
        max_notLy0 = list_notLy_values[0][0]
        max_notLy1 = list_notLy_values[0][1]
        if max_notLy0 < i[0]:
            max_notLy0 = i[0]
        if max_notLy1 < i[1]:
            max_notLy1 = i[1]


    if (max_isLy0 + max_mayLy0 + max_notLy0) == 0:
        wynik0 = 1
        wynik1 = 1
    else:
        wynik0 = ((0.11 * max_isLy0) + (0.5 * max_mayLy0) + (0.885 * max_notLy0)) / (max_isLy0 + max_mayLy0 + max_notLy0)
        wynik1 = ((0.11 * max_isLy1) + (0.5 * max_mayLy1) + (0.885 * max_notLy1)) / (max_isLy1 + max_mayLy1 + max_notLy1)
    
    #print("wynik: ",wynik0, ", ",wynik1)

    if wynik0 >= 0.5 and wynik1 >= 0.5:
        return 'notLy'
    else:
        return [wynik0, wynik1]