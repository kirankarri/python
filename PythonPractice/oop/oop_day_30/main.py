

try:
    file = open('test.txt','a')
except:
    print('file not found')
    file = open('test.txt','w')
else:
    file.write('something')
finally:
    file.write('Finally!')