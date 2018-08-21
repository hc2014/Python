WordCloud 是一个词云库

默认安装方式是:

```python
pip install WordCloud
```

结果没成功

然后用下载`whl`文件的方式来安装，[WordCloud](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)的版本太多了，所以要先看看pip支持哪些版本

```python
>>> import pip._internal
>>> print(pip._internal.pep425tags.get_supported())
[('cp35', 'cp35m', 'win32'), ('cp35', 'none', 'win32'), ('py3', 'none', 'win32'), ('cp35', 'none', 'any'), ('cp3', 'none', 'any'), ('py35', 'none', 'any'), ('py3', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), ('py31', 'none', 'any'), ('py30', 'none', 'any')]
>>>
```

可以看到的是支持`('cp35', 'cp35m', 'win32')`

然后在  [WordCloud](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud) 选择对应你的版本即可

```python
C:\Users\hc>pip install wordcloud-1.5.0-cp35-cp35m-win32.whl
Requirement 'wordcloud-1.5.0-cp35-cp35m-win32.whl' looks like a filename, but the file does not exist
Processing c:\users\hc\wordcloud-1.5.0-cp35-cp35m-win32.whl
Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: 'C:\\Users\\hc\\wordcloud-1.5.0-cp35-cp35m-win32.whl'


C:\Users\hc>pip install wordcloud-1.5.0-cp35-cp35m-win32.whl
Processing c:\users\hc\wordcloud-1.5.0-cp35-cp35m-win32.whl
Requirement already satisfied: numpy>=1.6.1 in d:\python\lib\site-packages (from wordcloud==1.5.0) (1.15.0)
Requirement already satisfied: pillow in d:\python\lib\site-packages (from wordcloud==1.5.0) (5.2.0)
Installing collected packages: wordcloud
Successfully installed wordcloud-1.5.0

C:\Users\hc>
```

安装的过程报错了一次，主要原因是widnows下载的文件默认是在`下载`目录里面，所以把东西移到`C:\\Users\\hc`下再次安装后就成功了