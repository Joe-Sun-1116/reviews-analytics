data = []
count = 0
length = 0

with open('053 reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		length += len(data[count])
		count += 1

	print('Read finish')
print('Average length :', length/len(data))
