n = 9

dwarf = []
for _ in range(n):
    dwarf.append(int(input("난쟁이 키 입력: ")))

total = sum(dwarf)
fake_dwarf = []


for i in range(n):
    for j in range(n):
        if dwarf[i] == dwarf[j] : continue
        
        elif total - ( dwarf[i] + dwarf[j]) == 100:
            fake_dwarf.append(dwarf[i])
            fake_dwarf.append(dwarf[j])
        
    if len(fake_dwarf) == 2:
        break

for dw in fake_dwarf:
    dwarf.remove(dw)


dwarf.sort()
print("------------------------------")
print("정답: :")
for df in dwarf:
    print(df)