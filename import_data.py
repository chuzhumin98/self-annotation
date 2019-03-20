#!/usr/bin/env python
# coding:utf-8

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "self-annotation.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import pickle as pkl

def load_object(path):
    with open(path, 'rb') as f:
        obj = pkl.load(f)
    return obj

def save_object(obj, path):
    with open(path,'wb') as f:
        pkl.dump(obj, f)

import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from Label.models import LabelAnnotation
    path = '/Users/chuzhumin/Documents/research/大四下/Noisy_label/object/queries_dict_withclick.pkl'
    queries_dict = load_object(path)
    for qid in queries_dict:
        print(qid)
        qcontent = queries_dict[qid]['content']
        print('qcontent: {}'.format(qcontent))
        for uid in queries_dict[qid]:
            if uid != 'content' and uid != 'content_split':
                LabelAnnotation.objects.create(qid=qid, qcontent=qcontent, uid=uid)


if __name__ == "__main__":
    main()
    print('Done!')