# 1. 创建虚拟环境
## 检查Python版本
`python3 --version`
## 2. 创建虚拟环境
`python3 -m venv env`
## 3. 安装依赖包
`cd mdict-utils`
`python setup.py install`
## 4. 编辑字典源文件
源文件位置：`my_dictionary/example_file.txt`
`python my_dictionary/file_utils.py`
## 5. 编译生成mdx文件
`mdict -a example.txt example.mdx`

