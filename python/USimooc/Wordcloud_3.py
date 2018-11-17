import wordcloud
import jieba
f = open("D:/TEST/test/python/USimooc/Doc/工作报告.txt", "r")
te = f.read()
f.close()
ls = jieba.lcut(te)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000,\
                        height=700, background_color="white")
w.generate(txt)
w.to_file("工作报告.png")
