import wordcloud
import jieba
txt = "增值税只对产品或者服务的增值部分纳税，\
减少了重复纳税的环节，是党中央、国务院，根据经济社会发展新形势，\
从深化改革的总体部署出发做出的重要决策。目的是加快财税体制改革、\
进一步减轻企业赋税，调动各方积极性，促进服务业尤其是科技等高端服务\
业的发展，促进产业和消费升级、培育新动能、深化供给侧结构性改革。"
w = wordcloud.WordCloud(width=400, height=300, font_path="msyh.ttc", background_color="white")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file('wordcloud.png')