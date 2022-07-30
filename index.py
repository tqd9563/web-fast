from multiprocessing.spawn import import_main_path
from pywebio.output import *
from pywebio.session import go_app
import os

def main():
    '''
    五分钟学会PyWebio
    '''
    pwd = os.getcwd()
    put_markdown('# 五分钟学会PyWebio')

    img = open(f'{pwd}/static/avatar.jpeg', 'rb').read()
    put_image(img, title='图片标题', width='296px', height='256px'),
    put_row(
        content=[
            put_markdown(
                mdcontent=r'''
                    这是我自学pywebio写的一个demo主页, 仅供自己学习参考~
                    ## 页面部署
                    这个网页是用的`path_deploy()`的方式部署的, 通过`put_link()`方法进行app之间的跳转, 文件结构如下图:
                '''
            ),
            put_link(name='关于此人', url='/about')
            # put_button(label='关于此人', onclick=lambda: go_app('about'))
        ],
        size=['95%', '5%']
    )

    
    img = open(f"{pwd}/static/structure.png", 'rb').read()
    put_image(img, width="220px", height="400px")
    put_markdown(
        mdcontent=r'''
            - libs: 包含了utils(一些常用函数、装饰器等)和code(输出原代码)
            - pages: 每个python文件都对应了一个页面, 其中均定义了一个名为`main`的
            pywebio的app。每个app反映在url的路径上为`<host>:<port>/pages/<pyfile_name>`
            - static: 存储一些静态资源例如图片文件
            - __main__.py: 主文件, 在这里通过`path_deploy()`进行部署。它会自动寻找项目中的所有`main`并解析
            - index.py: 主页文件, 其中的main()函数定义了主页的展示内容，对应的url路径则为`<host>:<port>/`
            - about.py: 关于本人, 其中的main()函数定义了一个自我介绍的页面，对应的对应的url路径则为`<host>:<port>/about`
            
            在这样的网页结构下, 与`__main__.py`同层级的python文件中，只要有定义pywebio app（比如`about.py`）就可以通过
            `<host>:<port>/<pyfile_name>`的路径来访问
        '''
    )

    put_markdown(r'''
        ## 简单的调查问卷
        可以通过`pywebio.input`这一交互输入模块来实现简单的web问卷。
    ''')
    put_row(put_link(name='这里是一个简单的例子', url='/pages/input'))
    put_markdown(
        mdcontent=r'''
            ## 内容输出
            在`pywebio.output`模块中定义了很多的静态内容输出函数，这里罗列了一些常见的输出格式：
        '''
    )
    put_row(put_link(name='内容输出示例', url='/pages/output'))
    put_markdown(
        mdcontent=r'''
            ## 交互式可视化
            pywebio支持第三方库的交互式可视化，诸如`pyecharts`，`plotly`，`cutecharts`，`bokeh`等。
        '''
    )
    put_row(put_link(name='可视化示例', url='/pages/plot'))
    