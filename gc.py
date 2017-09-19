
'''
create dictionary for file dataset
id = odd rows = keys
DNA strings = even rows = items
calculate GC content
'''

content_data = {}

data = open('rosalind_gc.txt').readlines()
ids = []
for string in data:
	index = data.index(string)
	if '>' in string:
		data[index] += '#'
		data[index-1] += '#'
		ids.append(string)

join_data = ''.join(data)
split_data = join_data.split('#')

print(ids)

total = []

for string in split_data:
	string = string.replace('\n', '')
	total.append(string)

print(total)

for dna_id in ids:
	index = total.index(dna_id.strip('\n'))
	print(index)
	dna_str = total[index+1]
	c = dna_str.count('C')
	g = dna_str.count('G')
	gc_content = (c + g) / len(dna_str)
	content_data[gc_content] = dna_id

print(content_data)

maximum = max(content_data.keys())
max_id = content_data[maximum]
print(max_id)
print(maximum*100)
