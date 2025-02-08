import random

def random4data():
    l = []
    for i in range(7):
        sl = []
        for j in range(5):
            sl.append(random.uniform(-20,10))
        l.append(sl)
    return l

# Generate the random data
random_data = random4data()
print(random_data)
