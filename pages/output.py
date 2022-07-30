from libs.util import show_code, back_home, clear_code, coding
from pywebio import start_server, config
from pywebio.output import *
from libs.code import *
import random
import time
import os

'''
内容输出
'''

@use_scope(name='tab')
@coding(scope='tab_code', code=TAB_CODE)
def output_tab():
    put_markdown(r'''
        ### 横向标签栏Tabs
        - 参数`tabs`由一组`{"title": xxx, "content": xxx}`组成的list构成
        - 其中`title`是每个Tab的标记, `content`是对应的内容
    
        更多详见[pywebio.output.put_tabs](https://pywebio.readthedocs.io/zh_CN/latest/output.html#pywebio.output.put_tabs)
    ''')
    put_tabs([
        {'title': 'Text', 'content': 'Hello world'},
        {'title': 'Markdown', 'content': put_markdown('~~Strikethrough~~')},
        {'title': 'More content', 'content': [
            put_table([
                ['Commodity', 'Price'],
                ['Apple', '5.5'],
                ['Banana', '7'],
            ]),
            put_link('pywebio', 'https://github.com/wang0618/PyWebIO')
        ]},
    ])


@use_scope(name='info')
@coding(scope='info_code', code=INFO_CODE)
def output_info():
    put_markdown('### 通知信息')
    put_grid(
        content=[
            [
                put_info('这是一段info, 颜色是蓝色', closable=False),
                put_warning('这是一段warning, 颜色是黄色, 点击×可关闭', closable=True)
            ],
            [
                put_error('这是一段error, 颜色是红色', closable=False),
                put_success('这是一段success, 颜色是绿色', closable=False)   
            ]
        ]
    )


@use_scope(name='processbar')
@coding(scope='processbar_code', code=PROCESSBAR_CODE)
def output_processbar(name, init, label, auto_close):
    '''
    输出进度条
    :param name: 名字
    :param init: 进度条起始位置
    :param label: 进度条显示的标签
    :param auto_close: 是否在进度结束后自动关闭
    '''
    put_markdown('### 进度条')
    put_processbar(name, init, label, auto_close)
    for i in range(11):
        set_processbar(name=name, value=i / 10)
        time.sleep(random.random() / 5)
    

@use_scope(name='table')
@coding(scope='table_code', code=TABLE_CODE)
def output_table():
    put_markdown(r'''
        ### 表格
        - 列表项可以是`list`或者`dict`；单元格内容可以是`string`或者`put_xxx()`
    ''')
    put_table(
        tdata=[
            ['曼联', 'Manchester United F.C.', '红魔'],
            ['切尔西', 'Chelsea F.C.', '蓝军'],
            ['利物浦', 'Liverpool F.C.', '红军'],
            ['曼城', 'Manchester City F.C.', '蓝月亮'],
        ], 
        header=['球队', '英文名', '绰号']
    )

@use_scope(name='image')
@coding(scope='image_code', code=IMAGE_CODE)
def output_image(path, width, height):
    '''
    显示图片
    :param path: 图片所在地址
    :param width: 图片宽度
    :param height: 图片高度
    '''
    put_markdown(r'''
        ### 打印图片
        - 参数`src`可以是图片的URL，也可以是图片的二进制内容，还可以是一个`PIL.Image.Image`实例
        - 参数`width`和`height`控制图片大小，可取值有"20%"或者"30px"
    ''')
    img = open(path, 'rb').read()
    put_image(img, title='图片标题', width=width, height=height)

@use_scope(name='download')
def output_download(path, filename):
    '''
    下载文件
    :param path: 文件路径
    :param filename: 下载保存的文件名
    '''
    put_markdown(r'''
        ### 下载文件
        - 和显示图片一样, 需要向参数`content`提供文件的二进制内容
        - 参数`name`表示下载后保存的文件名
        - 参数`label`表示下载链接的文字
    ''')
    file = open(path, 'rb').read()
    put_file(name=filename, content=file, label='点我下载鸡瑟斯表情包！')
    
def output_collapse(open=False):
    '''
    打印可折叠内容
    :param open: 是否默认打开
    '''
    put_markdown(r'''
        ### 可折叠内容
        - 参数`title`控制标题
        - 参数`open`控制内容是否默认折叠/打开
    ''')
    put_collapse(title='点我有惊喜', content='你是大傻蛋子吧？', open=open)


@use_scope(name='loading')
@coding(scope='loading_code', code=LOADING_CODE)
def output_loading():
    put_markdown(r'''
        ### 加载提示
        参数`shape`控制样式, 参数`color`控制颜色
    ''')
    shapes = ['border', 'grow']
    colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
    put_table([
        ['Shape\Color'] + colors,
        ['border'] + [put_loading(shape='border', color=color) for color in colors],
        ['grow'] + [put_loading(shape='grow', color=color) for color in colors],
    ])

@config(title='用config装饰后的标题', description="多种输出格式, 比如tab、code等")
def main():
    pwd = os.getcwd()
    output_image(path=f'{pwd}/static/goldenglow.jpeg', width='250px', height='250px')
    output_tab()
    output_info()
    output_loading()
    output_download(path=f'{pwd}/static/jises.png', filename='jises.png')
    output_table()
    output_collapse(open=False)
    output_processbar(name='我是进度条', init=0.1, label=None, auto_close=False)
    back_home()

# if __name__ == '__main__':
#     start_server(multiple_output, port=8082, debug=True, auto_open_webbrowser=True, remote_access=True)