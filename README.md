# 1. 创建虚拟环境
## 检查Python版本
`python3 --version`
## 2. 创建虚拟环境
`cd mdict-utils` </br>
`python3 -m venv env`
## 3. 安装依赖包
`python3 setup.py install`
## 4. 编辑字典源文件
源文件位置：`my_dictionary/example_file.txt`
'cd ..`
`python3 my_dictionary/file_utils.py`
## 5. 编译生成mdx文件
`cd my_dictionary`
`mdict -a example.txt example.mdx`
注意如果提示tgdm包，请更新pip最新，并安装此依赖包
`pip install tqdm`
