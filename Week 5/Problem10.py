import time
def main():
    numbers = []
    times = []
    for i in range(1, 101):
        start_time = time.time()
        numbers.append(i)
        end_time = time.time()
        times.append(end_time - start_time)
    for index, t in enumerate(times, start=1):
        print("Time taken to append ",index,f":{t:.10f} seconds")
        
if __name__=="__main__":
    main()
 
 # Time remains constant