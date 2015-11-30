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

# 去停词和换行符
# 统计词频
def word_count(text):
    # 词频阀值
    value = 10
    # 词频大于阀值的词集合
    sub_ref_word = set()
    # 分词
    text_words = list(jieba.cut(text, cut_all=False))
    word_freq = {}
    for word in text_words:
        if word != '\r\n' and word not in stop_word:
            freq = word_freq.setdefault(word, 0)
            word_freq[word] = freq + 1
            # 词频大于阀值value
            if freq + 1 > value and word not in sub_ref_word:
                sub_ref_word.add(word)
    return word_freq, sub_ref_word

# 读取文章
f_text = open('10.txt')
text = f_text.read().decode("gbk")
f_text.close()

wfreq = word_count(text)


# print(len(text_words))
# print(text_words)
# print(stop_word)
if __name__ == '__main__':

    # catg_word = []
    # 参考词汇，具体词汇的维度
    ref_word = set()
    # 统计字典，类别-->文本-->词-->词频
    catg_text_word_freq = {}
    # 类别i
    # for i in range(1, 10):
    for i in range(1, 10):
        # 每类的样本文章
        # for j in range(10, 2011):
        text_word_freq = {}
        # for j in range(10, 2000):
        for j in range(10, 20):
            print("i--->" + str(i) + ",j--->" + str(j))
            file_name = "../Reduced/C00000" + str(i) + "/" + str(j) + ".txt"
            f1 = open(file_name)
            text1 = f1.read()
            f1.close()

            word_freq_j, sub_ref_word_j = word_count(text1)  # 1.词频字典 2.频率大于一定值的词集合

            text_word_freq[j] = word_freq_j
            ref_word = ref_word | sub_ref_word_j

        catg_text_word_freq[i] = text_word_freq

    print(catg_text_word_freq)

    # for catg1, text_word_freq1 in catg_text_word_freq.iteritems():
    #     for text1, word_freq1 in text_word_freq1.iteritems():
    #         for word1, freq1 in word_freq1.iteritems():
    #             if freq1 > 10:
    #                 ref_word.append(word1)

    # print(ref_word)
    print("维度为" + str(len(ref_word)))
    y = []
    x = []
    for i in range(1, 10):
        for j in range(10, 20):
        # for j in range(10, 2000):
            print("i--->" + str(i) + "j--->" + str(j))
            dimension = 0
            vector = {}
            for word in ref_word:
                dimension += 1
                if word in catg_text_word_freq[i][j].keys():
                    vector[dimension] = catg_text_word_freq[i][j][word]
                else:
                    vector[dimension] = 0
            x.append(vector)
            y.append(i)

    print(y)
    print(x)

    # m = svm_train(y[:1000], x[:1000], "-c 4")
    # p_label, p_acc, p_val = svm_predict(y[1000:], x[1000:], m)
    m = svm_train(y[:10], x[:10], "-c 4")
    p_label, p_acc, p_val = svm_predict(y[10:], x[10:], m)
