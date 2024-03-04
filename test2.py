from random import sample

def scalar_product(vect_a, vect_b):
    res = 0
    for i in range(len(vect_a)):
            res += vect_a[i] * vect_b[i]
    return res

def norm(vector):
    res = 0
    for el in vector:
        res += el ** 2
    return res ** 0.5

def distance(vect_a, vect_b):
    norm_a = norm(vect_a)
    norm_b = norm(vect_b)
    if len(vect_a) != len(vect_b):
        print('векторы разной длины')
    elif norm_a == 0 or norm_b == 0:
        print('есть нулевой вектор')
    else:
        print('косинусное расстояние =', 1 - scalar_product(vect_a, vect_b) / (norm_a * norm_b))

vector_a = sample(range(-100, 101), 10)
vector_b = sample(range(-100, 101), 10)
print(f'A = {vector_a}\nB = {vector_b}')
distance(vector_a, vector_b)