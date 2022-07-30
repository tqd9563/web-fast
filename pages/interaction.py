from libs.util import back_home
from pywebio.output import *

'''
交互输出
'''

def output_toast():
    '''
    弹出通知信息
    :param content: 通知内容
    :param duration: 持续时间
    :param position: 弹出位置, 可选left, center和right
    :param color: 颜色, 可选info, error, warn和success, 或者是十六进制颜色编码
    '''
    def show_toast():
        toast(content='我是蓝色的info消息!', duration=1, position='left', color='info')
        toast(content='我是红色的error消息!', duration=3, position='center', color='error')
        toast(content='我是黄色的warn消息!', duration=2, position='right', color='warn')
        toast(content='我是绿色的success消息!', duration=4, position='center', color='success')

    put_row(
        [
            put_button(label='点我显示通知信息', onclick=lambda: show_toast(), color='primary'),
            put_link(name='更多详情见pywebio.output.toast', url='https://pywebio.readthedocs.io/zh_CN/latest/output.html#pywebio.output.toast')
        ]
    )


def output_popup(title, content, size, implicit_close, closable):
    '''
    显示弹窗
    :param title: 弹窗标题
    :param content: 弹窗内容
    :param size: 弹窗窗口大小, 可选large, small, normal
    :param implicit_close: 是否可以通过点击弹窗外的内容来关闭弹窗
    :param closable: 是否可由用户关闭弹窗
    '''
    def show_popup():
        popup(title, content, size, implicit_close, closable)
    
    put_row(
        [
            put_button(label='点我显示弹窗', onclick=lambda: show_popup(), color='secondary'),
            put_link(name='更多详情见pywebio.output.popup', url='https://pywebio.readthedocs.io/zh_CN/latest/output.html#pywebio.output.popup')
        ]
        
    )

def output_buttons():
    '''
    输出一组按钮
    '''
    put_markdown(
        mdcontent=r'''
            ### 输出一组按钮并绑定点击事件
            `buttons`和`actions`的区别是:
            - 前者的点击伴随着点击事件(即对应的回调函数)
            - 后者的点击只会对某个后台变量进行赋值, 如果需要触发事件需要写额外的代码

            **事实上，所有的输出都可以绑定一个`onclick`事件**
        '''
    )

    colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']

    @use_scope(name='buttons')
    def clear_button(x):
        clear(scope='buttons')
        put_buttons(
            buttons=[dict(label=c if c != 'dark' else 'clear', value=c, color=c) for c in colors], 
            onclick=lambda x: put_text(x, scope='buttons') if x != 'dark' else clear_button(x)
        )
    
    with use_scope(name='buttons'):
        put_buttons(
            buttons=[dict(label=c if c != 'dark' else 'clear', value=c, color=c) for c in colors], 
            onclick=lambda x: put_text(x, scope='buttons') if x != 'dark' else clear_button(x)
        )  

def main():
    output_toast()
    output_popup(
        title='你好! 瓜三娃!', 
        content='山东淄博',
        size='large', 
        implicit_close=True, 
        closable=True
    )
    output_buttons()
    back_home()