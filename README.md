# 安装指南
## 1. 拉取此项目
`git clone https://github.com/luckyJim-dev/mdict-utils.git`
## 2. 创建虚拟环境
### 检查Python版本
`python3 --version`
### 创建虚拟环境
`cd mdict-utils` </br>
`python3 -m venv env`
## 3. 安装依赖包
`source ./env/bin/activate` </br>
`python3 setup.py install`
## 4. 编辑字典源文件
源文件位置：`my_dictionary/example_file.txt` </br>
`python3 my_dictionary/file_utils.py`
## 5. 编译生成mdx文件
`cd my_dictionary` </br>
`mdict -a example.txt example.mdx` </br>
注意如果提示tgdm包，请更新pip最新，并安装此依赖包 </br>
`pip install tqdm`
# 更多
[制作词库教程](https://www.bilibili.com/video/BV1z34y1f7gS/?vd_source=fd4563490a26f945829ef0bfa7a8397c) | 
[欧路词典导入词库教程](https://www.bilibili.com/video/BV1R24y167hn/?spm_id_from=333.999.0.0&vd_source=fd4563490a26f945829ef0bfa7a8397c)

