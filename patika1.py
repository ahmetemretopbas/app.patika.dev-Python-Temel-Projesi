# -*- coding: utf-8 -*-


'''
1-Bir listeyi düzleştiren (düzleştirme) fonksiyonunda. Elemanları ([[3]] çok olabilecek, olmayan listeler) gibi şeylerden olabilir. Anlamı:
giriş: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

çıktı: [1,'a','cat',2,3,'dog',4,5]

2-erilen listenin personeline döndürülen bir program programı. Eğer listenin elemanlarının elemanlarının listesi, elemanların elemanlarını döndürün. Anlamı:
giriş: [[1, 2], [3, 4], [5, 6, 7]]

çıktı: [[[7, 6, 5], [4, 3], [2, 1]]

'''







# cevap 1:
    
x = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
f_list = []


def flatten_list(liste):
    for item in liste:
        if type(item) == list:
            flatten_list(item)
        else:
            f_list.append(item)


flatten_list(x)
print(f_list)
f_list.clear()



# cevap 2:
y_list = []  
def ex_list(liste2):
    for i in liste2:
        if i.sort(reverse = True):
            ex_list(i)
        else:
            y_list.append(i)
y = [[1, 2], [3, 4], [5, 6, 7]]
ex_list(y)
y_list.reverse()
print(y_list)
    
    
    
    
    
    
    
    
    