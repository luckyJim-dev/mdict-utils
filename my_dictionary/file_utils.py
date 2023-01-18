
class MdxItem:
    def __init__(self, key='', body=''):
        self.key = key
        self.body = body
    def to_mdx_txt(self):
        body_key ='<font size=5>{0}</font>'.format(self.key)
        mdx_txt = '{0}\r\n{1}\r\n<br>\r\n{2}</>'.format(self.key, body_key, self.body)
        return mdx_txt


def csv_to_mdx_txt(path_csv, path_txt):
    mdx_items = []
    with open(path_csv, encoding='utf-8') as f:
        for line in f.readlines():
            line.strip()
            [key,body] = line.split(',')
            mdx_item = MdxItem(key,body)
            mdx_item_txt = mdx_item.to_mdx_txt()
            mdx_items.append(mdx_item_txt)
            mdx_items_str = '\r\n'.join(mdx_items)
    with open(path_txt, 'w', encoding='utf-8') as f:
        print(mdx_items_str)
        f.write(mdx_items_str)

if __name__ == '__main__':
    path_csv = 'Mydictionary/example.csv'
    path_txt = 'Mydictionary/example.txt'
    csv_to_mdx_txt(path_csv, path_txt)