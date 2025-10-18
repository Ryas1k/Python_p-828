import  bisect 
from dict1 import frequency_pins, decimal_pins1, decimal_pins2

def frequency_defined(frequency):
    def frequency_get(range_frequency):
        if not range_frequency is None: 
            d =  frequency % 1000
            result = [9,28] # всегда штыри 9 и 28 подняты  
            result.extend(frequency_pins[range_frequency]['pins'])
            if 20000 <= frequency < 40000 and d in decimal_pins1:
                result.extend(decimal_pins1[d])
                result.sort()
                return result
            elif 40000 <= frequency and d in decimal_pins2:
                    result.extend(decimal_pins2[d])
                    result.sort()
                    return result
            else:
                    return None
                
    list_f_min = [r['min'] for r in frequency_pins]
    index = bisect.bisect_right(list_f_min, frequency)-1
    if index >= 0 and frequency <= frequency_pins[index]['max']:
        return frequency_get(index) 
    else: 
        return None

def process_frequency(frequency):
    index_range = frequency_defined(frequency) 
    return index_range


#Нахождение поднятых штырей по различной частоте 
print('Приветсвую в программе подбора штырей','для р-828',sep='\n')
while True:
    user = input("Введите частоту (например: 24050 Гц): ")
    try:
        f = int(user)
        if f == 0:
            break
        else:
            if process_frequency(f):
                print('Поднятые штыри: ',*process_frequency(f))
                print('Для выхода из программы введите 0')
            else:
                print('Частота не подходит. Смените частоту!!!') 
    except:
        print('Не зли меня, введи число!!!')


# python p-828.py 
# cd /путь/к/папке
# python3 моя_программа.py