from better_numbers import N

n = N(10)

for i in range(2, 11):
    print(n.to_base(i))

print()
for i in range(2, 11):
    print(N(i,i).to_base(10))
