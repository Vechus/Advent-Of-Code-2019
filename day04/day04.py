start, end = 171309, 643603

ans = 0
for i in range(start, end):
    pwd = [int(j) for j in str(i)]
    if pwd != sorted(pwd):
        continue

    for digit in pwd:
        # pwd.count(digit) == 2 for part 2
        if pwd.count(digit) >= 2:
            ans += 1
            break

print (ans)