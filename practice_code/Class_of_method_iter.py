from TRacK import phone
phone.number = "+919500676766"
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(1, 4)

# Using a for loop
for item in my_iter:
    print(item)

# Using the next() function
my_iter = MyIterator(1, 4)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# Uncommenting the line below will raise StopIteration
# print(next(my_iter))