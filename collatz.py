
def do_collatz(num):
    count = 1
    collatz_numbers = {num: count}
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        count += 1
        collatz_numbers[num] = count
    return collatz_numbers


sample = do_collatz(7)

do_collatz_flag = 0


for i in range(1, 1000, 2):
    if i % 8 == 1:
        print()
    if do_collatz_flag == 1:
        if i in sample:
            print(i, end="")
            print(f"({sample[i]})", end="\t")
    else:
        print(i, end="")
        if i % 2 == 0:
            print(f"({i // 2})", end="\t")
        else:
            j = 3 * i + 1
            while j % 2 == 0:
                j //= 2
            print(f"({j})", end="\t")



