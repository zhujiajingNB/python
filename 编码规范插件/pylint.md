## pylint

Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准和有潜在问题的代码。

#### pylint使用：

1. 安装pylint:pip install pylint

2. pycharm配置pylint

   ```
   File > Settings... > Tools > External Tools，点击 + 号添加，如下图配置
   ```

   ![img](https://upload-images.jianshu.io/upload_images/13606568-a98a1de37deb6d7b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1023/format/webp)

   ```
   Tool Settings 设置
   ```

   ```
   Program：C:\ProgramData\Anaconda3\Scripts\pylint.exe #pylint exe文件安装路径
   Arguments ：--output-format=parseable --disable=R --disable=C0102,C0103,C0111,C0301,C0302,C0303,C0304,C0305,W0120,W0123,W0401,W0603,W0612,W0614,W0621,W0622,W0703,E1003,E1101 $FilePath$
   Working directory： $FileDir$
   ```

   

   ![img](https://upload-images.jianshu.io/upload_images/13606568-57b8a67f36ca7207.png?imageMogr2/auto-orient/strip|imageView2/2/w/610/format/webp)

   3.使用pylint

   ​	Tools菜单下就会多出*pylint*工具了：

   ![img](https://upload-images.jianshu.io/upload_images/3795612-d13817495a4b88c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

   ​	

