import wordcloud
import jieba
from scipy.misc import imread
mask = imread("E:/local/test/Python/USimooc/Doc/fivestar.png")
f = open("E:/local/test/Python/USimooc/Doc/1号文件.txt", "r")
te = f.read()
f.close()
ls = jieba.lcut(te)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", mask=mask, width=1000,\
                        height=700, background_color="white",)
w.generate(txt)
w.to_file("1号文件.png")
