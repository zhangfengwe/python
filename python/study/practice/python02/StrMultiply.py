# 序列乘法运算示例
# 在屏幕中央且宽度适中的盒子中打印一个句子
# 要打印的句子
content = input('请输入要打印的句子： ')
# 屏幕宽度
screen_width = input('请输入屏幕宽度： ')
text_width = len(content)
box_width = text_width + int(screen_width) // 2
left_margin = (int(screen_width) - box_width) // 2

print()
print(' '* left_margin + '-' * box_width)
print(' '* left_margin + '|' + ' ' * (box_width - 2) + '|')
print(' '* left_margin + '|' + content.center(box_width - 2) + '|')
print(' '* left_margin + '|' + ' ' * (box_width - 2) + '|')
print(' '* left_margin + '-' * box_width)
print()
