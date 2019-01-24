class JustCount:
    __secret_count = 0   # 公有变量
    public_count = 0     # 私有变量

    def count(self):
        self.__secret_count += 1
        self.public_count += 1
        print(self.__secret_count)


counter = JustCount()
counter.count()
counter.count()
print(counter.public_count)
print(counter.__secret_count)    # 报错，实例不能访问私有变量
