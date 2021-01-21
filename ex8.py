formatter = "{} {} {} {}" #做好框，等待填进去，取代{}

print(formatter.format(1,2,3,4)) #数值不用双引号
print(formatter.format("one","two","three","four")) #字符串需要双引号才能填进去
print(formatter.format(True,False,True,True)) #布尔字符页不需要双引号
print(formatter.format(formatter,formatter,formatter,formatter)) #我填我自己，12个{}
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
)) #和教材不一样，为什么这里输出显示不换行？
