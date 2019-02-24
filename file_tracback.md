# 文件
- 读取整个文件。
    - with open('文件名.后缀') as file_object   返回一个文件对象存储在变量中
        - contents = file_object.read()
        - print(contents)
- 文件路径
    - 要让Python打开不与程序文件位于同一个目录的文件，需要提供文件路径。
    - 相对路径和绝对路径。
    
- 逐行读取
    - 使用for循环
- 创建已给包含文件各行内容的列表。
    - open()返回的文件对象只在with代码块内可用。如果要在外部使用需要将文件各行储存在列表中。
    - 使用readlines()从文件中读取每一行，并将其存储在一个列表中，然后可以逐行读取。 
- 写入文件
    - with open('文件名，'模式') as file_object:
        - file_object.write('内容')
        
    - 模式
        - 'w' 写入模式
        - 'r' 读取模式
        - 'a' 附加模式  内容附加到文件末尾，而不是覆盖文件原来的内容
        - '+' 
- 存储数据
    - 使用json.dump(存储的数据，用户存储的文件对象)和json.load()
    -  参看案例
- 重构
    - 将代码划分为一系列完成具体工作的函数。这样的过程被成为重构。    
        
# 异常
- 什么是异常？
    - python执行期间发生的错误，它是一个特殊的对象。
    - 异常是使用try-except代码块处理的。
    - 使用try-except代码块时，即便出现异常，程序也将继续运行。
- 处理ZeroDivisionError异常
    - try:
        - print(5/0)      
    - except ZeroDivisionError: 
        - print("you can't divide by zero")
- else代码块
    - try代码块成功执行的代码都应该放到else代码块中。
- try-except-else工作原理
    - python尝试执行try代码块的代码，只有可能引发异常的代码才需要放在try语句中。
    如果尝试成功，这些代码应该放在else中。
    except尝试告诉python如果发生异常该怎么办。
    
- 处理FileNotFoundError  无法找到文件
    