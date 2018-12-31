# -*- coding: utf-8 -*-
#/usr/bin/python2

from __future__ import print_function
from hyperparams import Hyperparams as hp
import random
import codecs
import os
from collections import Counter

def make_vocab():
    label_dict = Counter()
    vocab_dict = Counter()
    with open(hp.raw_data) as reader, open(hp.train_data, 'w') as train_writer, open(hp.test_data, "w") as test_writer, open(hp.valid_data, "w") as val_writer:
        for line in reader:
            line = line.strip("\r\n")
            if not line:
                continue
            ss = line.split(" ")
            if len(ss) < 11:
                continue
            label = ss[0]
            label_dict[label] += 1
            for hero in ss[1:]:
                vocab_dict[hero] += 1
            choice = random.randint(1, 10)
            if 1 == choice:
                test_writer.write("%s\n" % line)
            elif 2 == choice:
                val_writer.write("%s\n" % line)
            else:
                train_writer.write("%s\n" % line)

    if not os.path.exists('preprocessed'): os.mkdir('preprocessed')
    with codecs.open('preprocessed/hero-vocab.txt', 'w', 'utf-8') as fout:
        fout.write("{}\t1000000000\n{}\t1000000000\n{}\t1000000000\n{}\t1000000000\n".format("<PAD>", "<UNK>", "<S>", "</S>"))
        for word, cnt in vocab_dict.most_common(len(vocab_dict)):
            fout.write(u"{}\t{}\n".format(word, cnt))

    with codecs.open('preprocessed/total-labels.txt', 'w', 'utf-8') as fout:
        for word, cnt in label_dict.most_common(len(label_dict)):
            fout.write(u"{}\t{}\n".format(word, cnt))

if __name__ == '__main__':
    make_vocab()

    print("Done")