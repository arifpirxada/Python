from collections import OrderedDict

glossary=OrderedDict()

glossary['python']='language'
glossary['variable']='give name'
glossary['conditionals']='if and elif'
glossary['float']='decimal numbers'
glossary['string']='in words'
glossary['pass']='do nothing'

for key,value in glossary.items():
	print('word: '+key)
	print('meaning'+value)
	
#Below is the solution of 6-4 problem

glossary={
'python':'language',
'variable':'give name',
'conditionals':'if and elif',
'float':'decimal integers',
'string':'in words',
'pass':'do nothing'
}
for key,value in glossary.items():
	print('word: '+key)
	print('meaning: '+value