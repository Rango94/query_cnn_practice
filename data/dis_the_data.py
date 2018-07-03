import sys
cate={}
for line in open(sys.argv[1],'r',encoding='utf-8').readlines():
    cate[line.split('\t')[1].rstrip()]=1


querys_by_cate={}
for line in open(sys.argv[1],'r',encoding='utf-8').readlines():
    line=line.rstrip().split('\t')
    try:
        querys_by_cate[line[1]].append(line[0])
    except:
        querys_by_cate[line[1]]=[line[0]]


import random as rd
outfile_train=open('querys_train','w',encoding='utf-8')
#outfile_train.write('Descript,Category'+'\n')
outfile_test=open('querys_test','w',encoding='utf-8')
#outfile_test.write('Descript,Category'+'\n')

max_len=2*max([len(querys_by_cate[key]) for key in querys_by_cate])
print(max_len)
for key in querys_by_cate:
    num=0
    print(key+':',end='')
    flag=0
    for each in querys_by_cate[key]:
        if flag==0:
            outfile_test.write(each+'\t'+key+'\n')
            flag+=1
            continue
        if flag==1:
            outfile_train.write(each + '\t' + key + '\n')
            num+=1
            while rd.random()<0:
                outfile_train.write(each + '\t' + key + '\n')
                num+=1
            flag += 1
            continue
        else:
            if rd.random()>0.8:
                outfile_test.write(each + '\t' + key + '\n')
            else:
                outfile_train.write(each + '\t' + key + '\n')
                num+=1
                #print(((max_len-len(querys_by_cate[key]))/max_len))
                while rd.random()<((max_len-len(querys_by_cate[key]))/max_len):
                    outfile_train.write(each + '\t' + key + '\n')
                    num+=1
    print(num)




