from bitarray import bitarray

#zad 1
seed = 2;
prev_generated = seed;
def mult_generator(a, c, M):
    global prev_generated
    generated = (a * prev_generated + c) % M
    prev_generated = generated
    return generated / M


N = 10000
a = 69069
c = 1
M = pow(2, 32)

all_generated = []
for i in range(N):
    num = mult_generator(a, c, M)
    all_generated.append(num)

for i in range(100):
    print(all_generated[i])

in_015 = 0
for n in all_generated:
    if(n < 0.15):
        in_015 = in_015 + 1

print("Sprawdzenie: ", in_015 / N)

#zad 2
#N liczb ze zbioru 0_1

seed = [1,0,0,1,1,0,1,0,0,1,0]
arr = bitarray(seed)
#print(arr)
curr_index = 11

def register_generator(p, q):
    global curr_index
    generated = arr[curr_index - p] != arr[curr_index - q]
    arr.append(generated)
    curr_index = curr_index + 1
    return arr[curr_index - 1]

N=1000

zeros_num = 0
for i in range(100):
    p = 10
    q = 3
    result = register_generator(p, q)
    print(result)

for i in range(N):
    p = 10
    q = 3
    result = register_generator(p, q)
    if result == 0:
        zeros_num = zeros_num + 1

print("Sprawdzenie: ", zeros_num/N)


#Zad 1.d
print("Dodatki:")
def is_in_circle_middle(x,y):
    return pow(pow(x,2) + pow(y,2), 1/2.0) <= 1

def is_in_circle_vert(x,y, R):
    return pow(pow(x-1,2) + pow(y-1,2), 1/2.0) <= R

a = 69069
c = 1
M = pow(2, 32)
N = 100000
in_area = 0
R=1
for i in range(N):
    x = mult_generator(a, c, M) * 2 - 1
    y = mult_generator(a, c, M) * 2 - 1
    #print(x, y)
    if is_in_circle_vert(x,y,R) and is_in_circle_middle(x,y):
        in_area = in_area+1

print("Dodatek 1: ",(in_area/N) * 4)
    #print(is_in_circle_middle(x,y))
    #print(is_in_circle_vert(x,y,1))


#zad2.d

def gen_seq(N):
    p = 10
    q = 3
    res = []
    for i in range(N):
        res.append(register_generator(p, q))
    return res

def check_for_k(K, seq):
    ks = 0
    for i in range(len(seq)):
        if ks == K:
            return True
        if seq[i] == 1:
            ks = ks + 1
        else:
            ks = 0
    return False


N=10000
positive = 0
for i in range(N):
    seq = gen_seq(20)
    #print(seq)
    if check_for_k(5, seq) == True:
        positive = positive + 1

print("Dodatek 2: ", positive/N)








