
class MdxItem:
    def __init__(self, key='', body='', img_src='', author='249850395@qq.com'):
        self.key = key
        self.body_key = '<font size=5>{0}</font>'.format(self.key)
        self.body = body
        self.author='<br>\r\nupdated by {0}\r\n'.format(author)
        # self.img_src = '<img src="{0}}">'.format(img_src)
    def to_mdx_txt(self):
        mdx_txt = ''
        if not self.key:
            return mdx_txt
        mdx_txt = '{0}\r\n{1}\r\n<br>\r\n{2}{3}</>'.format(self.key, self.body_key, self.body, self.author)
        return mdx_txt

def csv_to_mdx_txt(path_csv, path_txt):
    mdx_items = []
    with open(path_csv, encoding='utf-8') as f:
        for line in f.readlines():
            line.strip()
            print(line)
            [key,body] = line.split(':')
            mdx_item = MdxItem(key,body)
            mdx_item_txt = mdx_item.to_mdx_txt()
            mdx_items.append(mdx_item_txt)
            mdx_items_str = '\r\n'.join(mdx_items)
    with open(path_txt, 'w', encoding='utf-8') as f:
        print(mdx_items_str)
        f.write(mdx_items_str)

if __name__ == '__main__':
    path_csv = 'my_dictionary/example_file.txt'
    path_txt = 'my_dictionary/example.txt'
    csv_to_mdx_txt(path_csv, path_txt)