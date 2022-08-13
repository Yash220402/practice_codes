power = int(input())
n = int(input())
enemy = list(map(int, input().strip().split(" ")))
current = power
fight_days = 0
for i in range(n):
    if current <= enemy[i]:
        fight_days = fight_days + 1
        current = power 
        if current <= enemy[i]:
            fight_days = -2
            break
    current = current - enemy[i]
print(fight_days+1)
