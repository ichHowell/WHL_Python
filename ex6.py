types_of_people = 10#创建了一个变量
x = f"There are {types_of_people} types of people."#f代表什么？与{}配套使用，字符串格式

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."#{}有什么作用？将字符串放在字符串里

print(x)
print(y)

print("I said: {x}")
print(f"I also said: '{y}'")#可以看出来有f和没有f的区别

hailarious = True
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hailarious))#.format()语法，另一种将字符串放在字符串里的方式

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)#+号起着结合的作用
