data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count=count+1 #也等於count += 1
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀取完了共有', len(data), '數據')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)
print('平均是', sum_len/len(data))
