#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "WangJing"
# Date: 18-8-2

# coding=utf-8
import os
import pandas as pd
def el(filepath):
    all_word = []
    pathDir = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir = os.path.join(filepath, s)  # 将文件名加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            if os.path.splitext(newDir)[1] == ".txt":  # 判断是否是txt
                with open(newDir, "r") as fin:
                    w_list = []
                    word = fin.read()
                    name = os.path.splitext(s)[0]
                    w_list.append(os.path.splitext(s)[0])
                    w_list.append(word)

                    all_word.append(w_list)

    #保存
    name = ['name','words']
    sord_save = pd.DataFrame(columns=name,data=all_word)
    sord_save.to_csv('transcript.csv',encoding='utf8',index = None)


el(u'/home/errolyan/github/Audio_txt/mic')
