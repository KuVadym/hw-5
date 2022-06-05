#Напишите реализацию функции factorize, которая принимает список чисел и возвращает список чисел,  done
#на которые числа из входного списка делятся без остатка.                                          done
#Реализуйте синхронную версию и измерьте время выполнения.                                         done?
#Потом улучшите производительность вашей функции, 
#реализовав использование нескольких ядер процессора для параллельных вычислений, и замерьте время выполнения опять.
#Для проверки правильности работы алгоритма самой функции можете воспользоваться тестом:           done
from multiprocessing import Process
import concurrent.futures
import time

arguments = (128, 255, 99999, 10651060)



def factorize(*number):             
    list_of_lists = []
    for num in number:
        num_list = []
        divisor = 1
        for el in range(num):
            if num % divisor == 0:
                num_list.append(divisor)
            divisor += 1 
        list_of_lists.append(num_list)
    return list_of_lists
    raise NotImplementedError()




if __name__ == '__main__':
    #First method - just func
    start_time = time.time()
    factorize(128, 255, 99999, 10651060)
    print(f"first method {(time.time() - start_time)} seconds")



    #Second method - with threading
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(factorize, arguments))
    print(f"second method {(time.time() - start_time)} seconds")


    #Third method - use processing
    start_time = time.time()
    processes = []
    for el in range(len(arguments)):
        process = Process(target=factorize, args=(arguments[el],))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
    
    print(f"third method {(time.time() - start_time)} seconds")
