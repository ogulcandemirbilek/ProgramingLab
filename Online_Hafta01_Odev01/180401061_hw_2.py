import sys,csv
def Histogram(list):
    fre={}
    for item in list:
        if(item in fre):
            fre[item] +=1
        else:
            fre[item] = 1
    return fre
def Median(Sirali):
    n = len(Sirali)
    if(n%2==1):
         middle = int(n/2)+1
         median = Sirali[middle-1]
    else:
         middle1 = int(n/2)-1
         middle2 = middle1+1
         median = (Sirali[middle1]+Sirali[middle2])/2
    return median
def ListeOrtalamasi(list1):
    a = len(list1)
    top=0
    ort=0
    for i in range (a):
        top+=list1[i]
    ort = int(top/a)
    return ort
def bubbleSort(my_List):
    n = len(my_List)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_List[j]<my_List[j+1]):
                temp = my_List[j]
                my_List[j] = my_List[j+1]
                my_List[j+1] = temp
    return my_List
with open(sys.argv[1]+"\\input_hw_2.csv","r") as file:
    dosya = csv.reader(file, delimiter=";")
    cikisTarihi=[]
    cikisAyi=[]
    for i in dosya:
       cikisTarihi = i[3].split("-")
       cikisAyi.append(cikisTarihi[1])
Histogram_cikisAyi = Histogram(cikisAyi)
listem = []
for i in Histogram_cikisAyi:
    listem.append( Histogram_cikisAyi[i])
Sirali = bubbleSort(listem)
Medyan = Median(Sirali)
Ortalama = ListeOrtalamasi(listem)
with open(sys.argv[2]+"\\180401061_hw_2_output.txt","w") as file:
    file.write("Medyan: "+str(Medyan)+"\n")
    file.write("Ortalama: "+str(Ortalama))    
