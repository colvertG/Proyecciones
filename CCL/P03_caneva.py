def main():
    archivo1 = open ('C:/Users/HP/Dropbox/FI/6to semestre/Cartografia/Tema 4/CCL/caneva.txt','a')
    for l in range(-121,-84):
        for l2 in range(11,36):
            archivo1.write('%s \t'%(l+121))
            archivo1.write('%s \t'%l)
            archivo1.write('%s \n'%l2)
    for l3 in range(11,36):
        for l4 in range(-121,-84):
            archivo1.write('%s \t'%(l3+26))
            archivo1.write('%s \t'%l4)
            archivo1.write('%s \n'%l3)
    archivo1.close()
main()