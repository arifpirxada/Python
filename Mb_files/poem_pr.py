with open('poems.txt') as f:
	n=f.read()
	if 'twinkle' in n:
		print('yes twinkle is present')
	else:
		print('no twinkle is not present')