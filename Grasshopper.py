count = int(input())
grains = list(map(int, input().split()))

maxCountGrains = 0
minCountGrains = 0
for i in range(0,count - 1):
    if grains[i] >= 0:
        maxCountGrains += grains[i]
    if grains[i] <= 0:
        minCountGrains += grains[i]
maxCountGrains += grains[-1]
minCountGrains += grains[-1]

print(maxCountGrains, minCountGrains)

