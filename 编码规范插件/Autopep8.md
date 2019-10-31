## Autopep8

Python语言的编码遵从PEP8规范，Autopep8工具能够依据PEP8规范，快速对代码文件进行规范检查并自动排版。对于变量名，类名，函数名等，会给出提示信息，需要工程师手动修改。

### autopepe8使用：

1. 安装autopep8: pip install autopep8

2. pycharm配置autopep8

   ```
   File -> Settings… ->Tools -> External Tools -> 点击“+”号添
   ```

   ![img](https://img2018.cnblogs.com/blog/1472349/201809/1472349-20180928211318318-937950836.png)

   ```
   Tool Settings 设置
   ```

   ```
   Name：autopep8
   
   Program：C:\ProgramData\Anaconda3\Scripts\autopep8.exe（在python的Scripts目录下）
   
   Arguments：--in-place --aggressive --aggressive $FilePath$
   
   Working directory：$ProjectFileDir$
   
   Output filters：$FILE_PATH$\:$LINE$\:$COLUMN$\:.*
   ```

   ![img](https://img2018.cnblogs.com/blog/1472349/201809/1472349-20180928211332298-1010225202.png)

   3.使用autopep8

   ​	右键点击需要规范的文件，在菜单中找到External Tools -> autopep8。完成！

   

   

   

