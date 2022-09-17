#task1_Machine learning
modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']
indices =[]
characters =[]
for i in modern_family:
    characters.append(i)
    indices.append(modern_family.index(i))
for i in range(len(characters)):
    characters[i] = characters[i].lower()
for j in range(len(characters)):
    characters[j] = characters[j].replace('_','-')
temp =[]
temp = map(lambda x : len(x),characters)
k =map(sum, zip(temp,indices))
indices = list(k)
indices.sort(reverse=True)
result = dict(zip(indices,characters))
print(result)


