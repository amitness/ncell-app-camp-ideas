with open('ideas.csv','r') as file:
    data = file.read()
listline = data.splitlines()

with open('newideas.csv','w') as newfile:
    for item in listline:
        pos1=item.find('""')
        if pos1>5:
            pos2=item.find('"',pos1+2)
            newfile.write(item[:pos1]+item[pos1+1:pos2]+' '+item[pos2+1:]+'\n')
        else:
            newfile.write(item+'\n')
