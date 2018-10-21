# encoding=utf-8
import wordcloud
import jieba
from scipy.misc import imread

mask = imread("D:/TEST/test/Python/USimooc/Doc/fivestar.png")
fed = open("D:/TEST/test/Python/USimooc/Doc/1号文件.txt", "r")
te = fed.read()
fed.close()
ls = jieba.lcut(te)
text = "  ".join(ls)
w = wordcloud.WordCloud(font_path="maya.ttc", mask=mask, width=1000, height=700, background_color="white" )
w.generate(text)
w.to_file('1号文件.png')
