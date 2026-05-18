import math

def is_prime(number):
    # Adım 1: Sayının 2'den küçük olup olmadığını kontrol et.
    # (Step 1: Check if the number is less than 2.)
    # Asal sayılar tanımı gereği 2 veya daha büyük olmalıdır.
    if number < 2:
        return False

    # Adım 2: Sayının 2 olup olmadığını kontrol et. 2 asal bir sayıdır.
    # (Step 2: Check if the number is 2. 2 is a prime number.)
    if number == 2:
        return True

    # Adım 3: Sayının çift olup olmadığını kontrol et (2'den büyükse).
    # (Step 3: Check if the number is even (if greater than 2).)
    # 2 dışındaki tüm çift sayılar asal değildir, çünkü 2'ye bölünebilirler.
    if number % 2 == 0:
        return False

    # Adım 4: 3'ten başlayarak sayının kareköküne kadar olan tek sayılarla bölünebilirliğini kontrol et.
    # (Step 4: Check divisibility by odd numbers starting from 3 up to the square root of the number.)
    # Bir sayının asal olup olmadığını kontrol ederken, sadece kareköküne kadar olan sayılara bakmak yeterlidir.
    # Ayrıca, 2'yi zaten kontrol ettiğimiz için sadece tek bölenleri kontrol etmemiz yeterlidir.
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2): # Sadece tek sayıları kontrol et (3, 5, 7, ...)
        if number % i == 0:
            return False

    # Adım 5: Yukarıdaki tüm kontrollerden geçtikten sonra sayı asaldır.
    # (Step 5: If the number passes all the above checks, it is prime.)
    return True

# Örnek kullanım:
# (Example usage:)
print(f"7 asal mı? {is_prime(7)}")      # Çıktı: 7 asal mı? True
print(f"10 asal mı? {is_prime(10)}")    # Çıktı: 10 asal mı? False
print(f"2 asal mı? {is_prime(2)}")      # Çıktı: 2 asal mı? True
print(f"1 asal mı? {is_prime(1)}")      # Çıktı: 1 asal mı? False
print(f"29 asal mı? {is_prime(29)}")    # Çıktı: 29 asal mı? True
print(f"99 asal mı? {is_prime(99)}")    # Çıktı: 99 asal mı? False
print(f"101 asal mı? {is_prime(101)}")  # Çıktı: 101 asal mı? True
