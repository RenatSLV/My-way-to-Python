import time 
import threading

def create_file(filename, content):
    """
    функция создает file
    """
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write(content)
        print(f'{filename} создан')

def work_create_file(index):
    """
    функция запускай фукцию котороя создаёт file
    """
    create_file(f'file {index}', 'content file')

start = time.time() #тамер начало

times = 100 #количество раз
threads = []

#многопоточность
for i in range(1, times + 1):
    thread = threading.Thread(target=work_create_file, args=(i,))
    threads.append(thread)
    thread.start()
    
end = time.time()   #таймер конец
result = end - start    #за какое время было создано 100 фаЙлов
print(f"время за которое было создано 100 файлов: {result}") # 00.6 сек