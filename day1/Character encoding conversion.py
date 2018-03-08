
### 字符编码转换

'''
python3 默认编码是utf-8
    内存中 字符串 编码是Unicode

python2 默认编码是ASCII
    内存中 字符串 默认是ASCII
    如果文件头申明了是GBK，那么字符串编码就是GBK

    Python2 中 Unicode 是单独的类型
'''

'''
python3 执行代码的过程:

    1.解释器找到代码文件，把代码字符串按文件头定义的编码加载到内存，转成unicode
    2.把代码字符串按照语法规则进行解释
    3.所有的变量字符都会以unicode编码声明
'''

# decode --> unicode --> encoding --> utf-8 --> decode --> unicode

'''
s = "派森"
print(s)
print(type(s))

s2 = s.decode("utf-8")
print(s2)
print(type(s2))

s3 = s2.encode("gbk")
print(s3)
print(type(s3))

s4 = s2.encode("utf-8")
print(s4)
print(type(s4))
'''
