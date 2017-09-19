foo = list('''string''')
rev_list = foo[::-1]
rev_str = ''.join(rev_list)

final = rev_str.replace('A', 'X').replace('T', 'A').replace('X', 'T')
final = final.replace('C', 'X').replace('G', 'C').replace('X', 'G')

print(final)