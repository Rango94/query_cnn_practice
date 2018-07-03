import numpy as np
import jieba as jb
import sys
import random as rd

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

    querys=open(filename,'r',encoding='utf-8').readlines()
    for i in range(len(querys)):
        idx1=rd.randint(0,len(querys)-1)
        idx2=rd.randint(0,len(querys)-2)
        tmp=querys[idx1]
        querys[idx1]=querys[idx2]
        querys[idx2]=tmp
    n=0
    for Idx,line in enumerate(querys):
        if Idx%5000==0 and Idx!=0:
            cate = np.array(cate)
            feature=np.array(feature)
            print(cate.shape)
            print(feature.shape)
            np.save('./data/'+filename + '_cate_'+str(n), cate)
            np.save('./data/'+filename+'_feature_'+str(n),feature)
            feature=[]
            cate=[]
            n+=1
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

    cate = np.array(cate)
    feature=np.array(feature)
    print(cate.shape)
    print(feature.shape)
    np.save('./data/'+filename + '_cate_'+str(n), cate)
    np.save('./data/'+filename+'_feature_'+str(n),feature)



if __name__=='__main__':
    #ans()
    build(sys.argv[1])




