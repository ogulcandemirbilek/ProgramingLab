#Lesson 1:
import random
my_list = [1,1,3,5,2,5,3,3,7,7,8,4]
def frequencyDictWithList(list):
    frequencyDict = {}
    for items in list:
        if(items in frequencyDict):
            frequencyDict[items] +=1
        else:
            frequencyDict[items]  = 1
    return frequencyDict #Dict ile bir listede ki elemanlardan kaçar tane olduğunu bulup yazdırma.
def frequencyListWithList(list1):
    frequencyList = []
    for i in range(len(list1)):
        s=False
        for j in range(len(frequencyList)):
            if(list1[i]==frequencyList[j][0]):
                frequencyList[j][1] += 1
                s = True
        if(s == False):
            frequencyList.append([list1[i],1])
    return frequencyList #Liste ile aynı işlemi yapma
print(frequencyDictWithList(my_list))
print(frequencyListWithList(my_list))
freqq = frequencyDictWithList(my_list)
frreq = frequencyListWithList(my_list)

#Lesson2: Mode bulma

def frequencyDictMode(fre):
    freMax = -1
    Mode = 1
    for key in fre.keys():
        if(fre[key]> freMax):
            freMax = fre[key]
            mode = fre[key]
    return mode,freMax #Dict yapısında mode bulma
def frequencyListMode(frre):
    frreMax = -1
    Mode = 1
    for item,frequency in frre:
        if(frequency>frreMax):
            frreMax = frequency
            mode = item
    return mode,frreMax #List Yapısıyla (tuple) mode bulma   
print(frequencyDictMode(freqq))
print(frequencyListMode(frreq))

#Lesson3: Liste de eleman arama yöntemleri:
# Linear Search:
def myLinearSearch(listt,itemSearch):
    found = (-1,-1) #eğer liste de yoksa default olucak
    n = len(listt)
    for indis in range(n):
        if (listt[indis] == itemSearch):
            found=(listt[indis],indis) #(bulunan sayı,indis) tuple şeklinde return edlir.
            #eğer buraya break koyarsak liste de aranan kelimeyi ilk bulduğu indisi yazar.
    return found
print(myLinearSearch(my_list,7))
# Bubble Sort:
def bubbleSort(my_List):
    n = len(my_List)
    print(my_List)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_List[j]<my_List[j+1]):
                temp = my_List[j]
                my_List[j] = my_List[j+1]
                my_List[j+1] = temp
    return my_List
# Binary Search List:
def binarySearch(Liste,itemSearch):
    n = len(Liste)
    found=(-1-1)
    low = 0
    high = n-1
    while low<=high:
        mid = (high+low)//2
        if Liste[mid] == itemSearch:
            return Liste[mid],mid
        elif Liste[mid] > itemSearch:
            high = mid+1
        else:
            low = mid-1
    return found #bu dönerse aradığımız yok anlamına gelir ve (-1,-1) şeklinde geri döner.   
print(bubbleSort(my_list))
SiraliList = bubbleSort(my_list)
print(binarySearch(SiraliList,7))
 # Median Bulma:
def medianOfList(Sirali):
     n = len(Sirali)
     if(n%2==1):
         middle = int(n/2)
         median = Sirali[middle]
     else:
         middle1 = Sirali[int(n/2)]
         middle2 = Sirali[int(n/2)+1]
         median = (middle1+middle2)/2
     return median
print(medianOfList(SiraliList))
