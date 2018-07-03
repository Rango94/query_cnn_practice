import numpy as np
import os

class data_helper:
    test_file_num=0
    train_file_num=0
    now_file_num =0
    now_batch_num=0
    batch_size=0
    train_featrue_file_list={}
    train_cate_file_list={}

    test_featrue_file_list = {}
    test_cate_file_list = {}
    remain_feature=0
    remain_cate=0

    def __init__(self):
        filename_all = os.listdir('./data/data')
        test_file=[i for i in filename_all if 'test' in i]
        train_file=[i for i in filename_all if 'train' in i]
        self.test_file_num=len(test_file)/2
        self.train_file_num=len(train_file)/2
        self.now_file_num = 0
        self.now_batch_num = 0
        self.batch_size=100

        for i in test_file:
            i_=i.rstrip('.npy')
            if 'feature' in i:
                self.test_featrue_file_list[i_.split('_')[-1]]=i
            if 'cate' in i:
                self.test_cate_file_list[i_.split('_')[-1]]=i

        for i in train_file:
            i_=i.rstrip('.npy')
            if 'feature' in i:
                self.train_featrue_file_list[i_.split('_')[-1]]=i
            if 'cate' in i:
                self.train_cate_file_list[i_.split('_')[-1]]=i

        self.remain_feature=np.load(self.train_featrue_file_list[self.now_file_num])
        self.remain_cate=np.load(self.train_cate_file_list[self.now_file_num])

    def set_batch_size(self,n):
        self.batch_size=n

    def next_batch(self):
        try:
            featrue=self.remain_feature[self.now_batch_num:self.now_batch_num+self.batch_size]
            cate=self.remain_cate[self.now_batch_num:self.now_batch_num+self.batch_size]
            self.now_batch_num+=self.batch_size
        except:
            featrue = self.remain_feature[self.now_batch_num:len(self.remain_feature)]
            cate = self.remain_cate[self.now_batch_num:len(self.remain_cate)]

            self.now_file_num+=1
            if self.now_file_num>=self.train_file_num:
                self.now_file_num=0
            self.remain_feature = np.load(self.train_featrue_file_list[self.now_file_num])
            self.remain_cate = np.load(self.train_cate_file_list[self.now_file_num])

            remain_num=self.batch_size-(len(self.remain_feature)-self.now_batch_num)
            self.now_batch_num=0
            featrue=np.concatenate(featrue,self.remain_feature[self.now_batch_num:self.now_batch_num+remain_num])
            cate = np.concatenate(cate, self.remain_cate[self.now_batch_num:self.now_batch_num + remain_num])
            self.now_batch_num+=remain_num

        return featrue,cate














