IMAGE_CODE = r'''
    img = open(path, 'rb').read()
    put_image(img, title='图片标题', width=width, height=height)
'''

TAB_CODE = r'''
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
'''

INFO_CODE = r'''
    put_grid(
        [
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
'''

PROCESSBAR_CODE = r'''
    put_processbar(name='我是进度条', init=0.1, label=None, auto_close=False)
    for i in range(11):
        set_processbar(name='我是进度条', value=i / 10)
        time.sleep(random.random())
'''

LOADING_CODE = r'''
    shapes = ['border', 'grow']
    colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
    put_table([
        ['Shape\Color'] + colors,
        ['border'] + [put_loading(shape='border', color=color) for color in colors],
        ['grow'] + [put_loading(shape='grow', color=color) for color in colors],
    ])
'''

TABLE_CODE = r'''
    put_table(
        tdata=[
            ['曼联', 'Manchester United F.C.', '红魔'],
            ['切尔西', 'Chelsea F.C.', '蓝军'],
            ['利物浦', 'Liverpool F.C.', '红军'],
            ['曼城', 'Manchester City F.C.', '蓝月亮'],
        ], 
        header=['球队', '英文名', '绰号']
    )
'''