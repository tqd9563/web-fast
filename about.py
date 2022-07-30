from pywebio.output import *
from pywebio import config
from libs.util import back_home

@config(title='about', description=None)
def main():
    put_markdown(r'''
        # 关于本人
        笨蛋一个
    ''')
    back_home()