#\这个字符可以把没法输入的字符转化成字符串
#转义符，将输入的字符转化为字符串
tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."#帮助把\打印出来

fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t*Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("I'm 6'2\"tall.")#\"加斜杠可以帮助把"打印出来
