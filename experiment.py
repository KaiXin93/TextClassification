# encoding=utf-8
__author__ = 'qkx'
from svmutil import *
import jieba

# 读取停词
f_stop = open('stop_words_ch_utf-8.txt')
stop_word = f_stop.read().decode('utf-8').split('\n')
f_stop.close()
stop_word.append(u'\n')
# print(stop_word)

# 读取文章
f_text = open('10.txt')
text = f_text.read().decode("gbk")
f_text.close()

text_words = list(jieba.cut(text, cut_all=False))

# 去停词和换行符
# 统计词频
i = 0
word_freq = {}
for word in text_words:
    if word != '\r\n':
        i += 1
        if word not in stop_word:
            freq = word_freq.setdefault(word, 0)
            word_freq[word] = freq + 1



# print(len(text_words))
# print(text_words)
# print(stop_word)
print(word_freq)
print(len(word_freq))
