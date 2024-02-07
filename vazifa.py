# 1-misol
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password(10)
print("Yangi parol:", password)
# 2-misol
def generate_even_numbers(up_to):
    return [num for num in range(2, up_to + 1, 2) if num % 2 == 0]

try:
    input_number = int(input("Juft sonlarni qaytarish uchun biror butun son kiriting: "))
    even_numbers = generate_even_numbers(input_number)
    print(f"Kiritilgan raqamgacha bolgan juft sonlar: {even_numbers}")
except ValueError:
    print("Faqat butun son kiritishingiz mumkin.")
# 3-misol
def toq_son_generator(boshlangich_raqam):
    raqam = boshlangich_raqam
    while True:
        if raqam % 2 != 0:
            yield raqam
        raqam += 1

boshlangich_raqam = int(input("Boshlang'ich raqamni kiriting: "))
generator = toq_son_generator(boshlangich_raqam)

for _ in range(10):
    toq_son = next(generator)
    print(toq_son)
# 4-misol
def tub_son_generator(boshlangich_raqam):
    raqam = boshlangich_raqam
    while True:
        if raqam > 1:
            tub = True
            for i in range(2, int(raqam**0.5) + 1):
                if raqam % i == 0:
                    tub = False
                    break
            if tub:
                yield raqam
        raqam += 1

boshlangich_raqam = int(input("Boshlang'ich raqamni kiriting: "))
generator = tub_son_generator(boshlangich_raqam)

for _ in range(10):
    tub_son = next(generator)
    print(tub_son)


