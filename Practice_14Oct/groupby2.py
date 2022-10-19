import itertools
output = itertools.groupby(range(12),lambda x:x//5)
print(list(output))
# for key, igroup in itertools.groupby(range(12), lambda x: x // 5):
#      print (key, list(igroup))

