
sentence = raw_input("sentence:")

screen_width = 180
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print
print ' ' * left_margin + '+' + '-' * (box_width + 12) + '+'
print ' ' * (left_margin + 4) + '| ' + ' ' * text_width + ' |'
print ' ' * (left_margin + 4) + '| '     + sentence     + ' |'
print ' ' * (left_margin + 4) + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '+' + '-' * (box_width + 12) + '+'
print