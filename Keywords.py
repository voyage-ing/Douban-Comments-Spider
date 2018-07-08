import re
import jieba
import pandas
import numpy
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud

def keywords(subpath):
    """
    :function: 将保存在文件中的评论信息，进行清洗。清洗出的关键词生成词云。
    """
    commentFile = subpath + ".txt"
    WC_img = subpath + "_WC.png"
    with open(commentFile,'r') as f:
        comments = f.readlines()
    com = ''.join(comments).split()
    comment = ''.join(com)

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern,comment)
    cleaned_comments = ''.join(filterdata)
    print(cleaned_comments)

    segment = jieba.lcut(cleaned_comments)
    words_df = pandas.DataFrame({'segment':segment})

    stopwords = pandas.read_csv("ChineseStopWords.txt",index_col=False,quoting=3,sep='\t',names=['stopword'],encoding='GB2312')
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

    # 用词云进行显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)
    word_frequence_list = dict(word_frequence_list)
    #print(word_frequence_list)
    wordcloud = wordcloud.fit_words(word_frequence_list)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file(WC_img)