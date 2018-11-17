import wordcloud
import jieba
f = open("D:/TEST/test/python/USimooc/Doc/1号文件.txt", "r")
te = f.read()
f.close()
ls = jieba.lcut(te)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000,\
                        height=700, background_color="green",\
                        max_words=15)
w.generate(txt)
w.to_file("1号文件.png")
