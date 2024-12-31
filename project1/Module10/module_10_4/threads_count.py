from threading import Thread
import json
import datetime

# Вся информация, что есть
res = []

# Список тредов
threads = []

# Список файлов
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def worker(file):
    with open(file, 'r') as f:
        js = json.load(f)
        res.extend(js)


def main():
    start = datetime.datetime.now()

    for i in range(len(files)):
        t = Thread(target=worker, args=(files[i],))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end = datetime.datetime.now()
    sum(res)
    return end - start


time_calc = []

for i in range(100):
    res = []
    time_calc.append(main())

print(sum([calc.microseconds for calc in time_calc])/len(time_calc)) # 29454.03
