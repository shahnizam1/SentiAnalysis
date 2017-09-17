#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-17
# @Author  : CKCZZJ
import os, sys
import numpy as np
import gzip


class WordEmbedding(object):
    def __init__(self, fname):
        with open(fname,'r') as fin:
            line=fin.readline()
            self._dict_size,self._embed_dim=[int(s) for s in line.split()]  #311467  50
            self._embedding=np.zeros((self._dict_size,self._embed_dim),dtype=np.float32)
            self._word2index=dict()
            self._index2word=[]
            for i in range(self._dict_size):
                line=fin.readline()[::-1].split(maxsplit=50)
                self._word2index[line[50][::-1]]=i   #line[0]是单词
                self._index2word.append(line[50][::-1])
                self._embedding[i,:]=np.array([float(x[::-1]) for x in line[::-1][1:51]])  #读入矩阵

    # Getters
    def dict_size(self):
        return self._dict_size

    def embedding_dim(self):
        return self._embed_dim
    
    def words(self):
        return self._word2index.keys()

    @property
    def embedding(self):
        return self._embedding
    
    def word2index(self,word):
        idx=-1
        try:
            idx=self._word2index[word]
        except KeyError:
            idx=self._word2index['unknown']
        return idx

    def index2word(self,index):
        assert 0<=index<self._dict_size
        return self._index2word[index]

    def wordvec(self,word):
        idx=self.word2index(word)
        return self._embedding[idx]