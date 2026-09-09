

# USING LIST COMPREHENSION

odd_square = [x * x for x in range(1,11) if x % 2 == 1]

print(odd_square)

# USING FOR LOOP

odd_square = []
for i in range(1,11):
    if i % 2 == 1:
        odd_square.append(i * i)
        
print(odd_square)