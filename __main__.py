from pywebio import start_server, config
from pywebio.platform import path_deploy
from os import path

# from pages.index import main as main_index
from index import main as main_index
from pages.output import main as multiple_output


# # 用start_server部署多个pywebio app并且实现相互跳转
'''
- 每一个app都可以用config装饰器来装饰，其`title`属性就是最后显示在网页上的链接名称。
- 如果不用@config装饰, 那显示的网页链接名称就是这个app对应的函数的docstring
- 这种方法的一个比较大的缺点是：标题好像无法自定义，必须是"Application index"。。
'''
# if __name__ == '__main__':
#     app = {
#         'main': main_index,     # 跳转链接是 http://localhost:<port>/?app=main
#         'multiple_output': multiple_output,  # 跳转链接是 http://localhost:<port>/?app=multiple_output
#     }
#     start_server(app, port=8082, debug=True, auto_open_webbrowser=True, remote_access=True)

# 用path_deploy部署多个pywebio app并且实现相互跳转
'''
- 更自由，可以更加定制化显示内容
- 要求: 每个app都对应某一个python文件里的main函数
'''
if __name__ == '__main__':
    cur_dir = path.dirname(path.abspath(__file__))
    print(f'cur_dir={cur_dir}')

    path_deploy(cur_dir, port=8082, debug=True)