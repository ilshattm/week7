def get_phibo(n):
    if n < 3:
        return 1
    else:
        last = (get_phibo(n - 1))
        last1 = (get_phibo(n - 2))
        rezult = last + last1
        print(rezult)
        return rezult

print(get_phibo(5))