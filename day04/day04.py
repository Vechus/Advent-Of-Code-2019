f = open("in04.txt", "r")
nums = f.readline().split(',')
start = int(nums[0])
end = int(nums[1])

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
