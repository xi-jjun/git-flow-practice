class User(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.sdfsdf = 1234

    def hello(self):
        print(f'저는 {self.name} 입니다. 안녕하세요')
