data = []
count = 0
with open('053 reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 2000 == 0:
			print(len(data))

print(data[0])
print('--------------------------------------')
print(data[93])