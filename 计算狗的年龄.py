age = int(input('请输入你家狗狗的年龄：'))
if age < 0:
    print('你是在逗我吧！')
elif age == 1:
    print('相当于14岁的人。')
elif age == 2:
    print('相当于22岁的人。')
elif age > 2:
    human = 22 + (age -2)*5
    print('对应人的年龄：',format(human))
          
