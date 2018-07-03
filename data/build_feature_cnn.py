import numpy as np
import jieba as jb
import sys


def ans():
    cate_dic={}
    word_dic={}
    cate_n=0
    word_n=0
    for line in open('querys_all','r',encoding='utf-8').readlines():
        line=line.rstrip().split('\t')
        if line[1] not in cate_dic:
            cate_dic[line[1]]=cate_n
            cate_n+=1
        for i in jb.cut(line[0]):
            if i not in word_dic:
                word_dic[i]=word_n
                word_n+=1

    with open('querys_dic','w',encoding='utf-8') as fo:
        for cate in cate_dic:
            fo.write(cate+'&:'+str(cate_dic[cate])+'|-|')
        fo.write('\n')
        for word in word_dic:
            fo.write(word+'&:'+str(word_dic[word])+'|-|')

def build(filename):
    feature=[]
    cate=[]
    cate_dic={}
    word_dic={}
    for idx,line in  enumerate(open('querys_dic','r',encoding='utf-8').readlines()):
        if idx==0:
            line=line.rstrip().rstrip('|-|').split('|-|')
            for each in line:
                each=each.split('&:')
                cate_dic[each[0]]=int(each[1])
        if idx==1:
            line=line.rstrip().rstrip('|-|').split('|-|')
            for each in line:
                each=each.split('&:')
                word_dic[each[0]]=int(each[1])

    for line in open(filename,'r',encoding='utf-8').readlines():
        query,cate_s=line.strip().split('\t')
        tmp=np.zeros((12,len(word_dic)))
        for idx,word in enumerate(jb.cut(query)):
            if idx==12:
                break
            tmp[idx,word_dic[word]]=1
        feature.append(tmp)
        cate_tmp=np.zeros(len(cate_dic))
        cate_tmp[cate_dic[cate_s]]=1
        cate.append(cate_tmp)

    feature=np.array(feature)
    cate=np.array(cate)
    print(feature.shape)
    print(cate.shape)
    np.save(filename+'_feature',feature)
    np.save(filename+'_cate',cate)


if __name__=='__main__':
    #ans()
    build(sys.argv[1])




