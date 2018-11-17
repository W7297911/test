import wordcloud
txt = "lift is short, you need python. if python is python"
c = wordcloud.WordCloud(background_color="white")
c.generate(txt)
c.to_file('wordcloud.png')