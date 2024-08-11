n = 10
skip_no = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == skip_no:
            continue
        if i == skip_no:
            continue
        print(i * j)

        