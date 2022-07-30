from pywebio.output import *

@use_scope(name='back')
def back_home():
    '''
    两种写法都可以
    '''
    # put_link(name='返回首页', url='/modules/index')
    put_link(name='返回首页', url='/', position=-1)

def show_code(scope, code, language):
    '''
    按下「显示代码」按钮后, 显示对应的代码, 并且在原来按钮的边上显示一个「隐藏代码」的按钮
    :param: scope: 当前输出域
    :param: code: 具体代码
    :param: language: 语言类型
    '''
    clear(scope='back')     # 先清空「返回首页」
    clear(scope=scope)      # 再清空两个按钮和代码所在的输出域
    with use_scope(name=scope):
        put_row(
            content=[
                put_button(
                    label="显示代码", 
                    onclick=lambda: show_code(scope=scope, code=code, language=language), 
                    color='primary',
                    outline=True
                ),   # 「显示代码」的按钮
                put_button(
                    label="隐藏代码", 
                    onclick=lambda: clear_code(scope=scope, code=code, language=language),
                    color='secondary', 
                    outline=True, 
                    position=1
                )   # 「隐藏代码」的按钮, 注意position
            ],
            scope=scope
        )
        put_code(content=code, language=language, scope=scope)  # 输出代码
    
    back_home()


def clear_code(scope, code, language):
    '''
    按下「隐藏代码」按钮后, 清空对应代码, 保留「显示代码」的按钮
    :param scope: 代码对应的输出域
    :param: code: 具体代码
    :param: language: 语言类型
    '''
    clear(scope=scope)      # 先清空整个输出域, 包括两个按钮以及代码
    put_button(
        label="显示代码", 
        onclick=lambda: show_code(scope=scope, code=code, language=language), 
        color='primary',
        outline=True,
        scope=scope
    )   # 「显示代码」的按钮


def coding(scope, code, language="python"):
    '''
    装饰器, 用于给某个pywebio的app加上下面的功能:
    1. 提供一个「显示代码」按钮, 按下按钮后, 打印这部分的源码, 并在该按钮旁显示一个「隐藏代码」的按钮
    2. 按下「隐藏代码」按钮后, 清空对应代码, 但保留「显示代码」的按钮
    '''
    def decorator(func):
        def wrap(*args, **kwargs):
            # 先执行原始函数func, 然后在末尾增加按钮
            func(*args, **kwargs)
            with use_scope(name=scope):
                put_button(
                    label="显示代码", 
                    onclick=lambda: show_code(scope=scope, code=code, language=language), 
                    color="primary",
                    outline=True,
                    scope=scope
                )
            put_markdown('---')
            
            return
        
        return wrap
    
    return decorator