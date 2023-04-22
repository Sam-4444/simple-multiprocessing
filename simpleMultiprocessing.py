import time
from multiprocessing import Process
from multiprocessing import freeze_support


def show(z):
    print(f"starting  {z}")
    time.sleep(2)
    print(f"ending {z}")

def main():
    freeze_support()
    start = time.perf_counter()

    p1 = Process(target=show, args=("eins",))
    p2 = Process(target=show, args=("zwei",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f"delay is : {end - start}")
if __name__ == "__main__":
    main()
