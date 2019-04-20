from gensim import corpora, models
import jieba.posseg as jp, jieba
# 文本集
outfilename="文件"
outputs=open(outfilename,'r',encoding='UTF-8')
words_list=[]
for lines in outputs.readlines():
    lines=lines.replace("\n","").split()
    words_list.append(lines)




dictionary = corpora.Dictionary(words_list)
# 基于词典，使【词】→【稀疏向量】，并将向量放入列表，形成【稀疏向量集】
corpus = [dictionary.doc2bow(words) for words in words_list]
# lda模型，num_topics设置主题的个数
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)
# 打印所有主题，每个主题显示4个词
for topic in lda.print_topics(num_words=1):
    print(topic)
# 主题推断
print(lda.inference(corpus))
outputs.close()
