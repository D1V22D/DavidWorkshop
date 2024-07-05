# Import time module
import time
a = [ i for i in range(100000)]
start = time.time()
for i in range(100000):
    if i < 100000:
        print(f" {i} ",end="")
    else:
        break
end = time.time()
print(f"\nthe execution time is {end - start}")
