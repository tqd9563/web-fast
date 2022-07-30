from libs.util import back_home
from pywebio.output import *
from pywebio.input import *

def personal_info_query():
    '''
    用户基本信息
    '''
    data = input_group(
        label='用户调研问卷',
        inputs=[
            input('请输入您的姓名', name='name', type=TEXT, required=True),
            # validate参数用于校验输入的合法性. 当输入值有效时返回None
            input('请输入您的年龄', name='age', type=NUMBER, validate=lambda x: '年龄必须大于零!' if x < 0 else None, required=True),
            radio(
                '您的性别是', 
                options=[
                    {'label': '男', 'value': '男', 'selected': True},
                    {'label': '女', 'value': '女'}, 
                    {'label': '其他', 'value': '其他'},
                ],
                inline=True,
                multiple=False,
                required=True,
                name='sex'
            ),
            radio(
                '您的职业是?', 
                options=['在读学生', '算法工程师', '数据分析师', '运维工程师', '客户端开发工程师', '服务器开发工程师', '产品经理', '其他'],
                multiple=False,
                inline=False,
                required=True,
                name='job'
            )
        ]
    )
    
    return data
    
def if_2cy():
    data = radio(
        '您是否是二次元?', 
        options=['是', '否'],
        multiple=False,
        inline=True,
        required=True
    )

    return data

def query_2cy():
    '''
    二次元相关问题
    '''
    anime_mapping = {
        '少年热血': ['海贼王', '火影忍者', '死神', '名侦探柯南'],
        '少女恋爱': ['龙与虎', '好像告诉你', '邻座的怪同学', '华丽的挑战'],
        '轻松日常': ['日常', '喵帕斯', '轻音少女', ''],
        '体育竞技': ['灌篮高手', '青之芦苇', '星合之空', '强风吹拂', '排球少年'],
        '恐怖悬疑': ['寒蝉鸣泣之时', '尸体派对', '尸鬼', '海猫鸣泣之时']
    }
    animes = list(anime_mapping.keys())

    data = input_group(
        label='',
        inputs=[
            select(
                '您最喜欢看什么类型的日漫?(单选)',
                options=['热血冒险', '少女恋爱', '轻松日常', '恐怖悬疑', '体育竞技'],
                onchange=lambda x: input_update('animation', options=anime_mapping[x]),
                multiple=False,
                inline=False,
                name='animation_type'
            ),
            select(
                '您喜欢的该类型日漫有',
                options=anime_mapping[animes[0]],
                multiple=True,
                name='animation'
            ),
            checkbox(
                '您喜欢下面哪些国漫?(可多选)',
                options=['狐妖小红娘', '风灵玉秀', '京剧猫', '一人之下', '魁拔', '我不喜欢国漫'],
                name='guoman'
            )
        ]
    )

    return data

def sdzb():
    clear(scope='back')
    with use_scope(name='back'):
        put_markdown('傻蛋子吧，怎么可能真的会抽奖啊')
    back_home()

def lottery():
    put_button('点击抽奖', onclick=sdzb, outline=True, color="success")

def main():
    '''
    一个简单的个人问卷
    '''
    data = personal_info_query()
    params = {
        'name': data['name'],
        'age': data['age'],
        'sex': data['sex'],
        'job': data['job'],
    }
    flag_2cy = if_2cy()
    params['flag_2cy'] = flag_2cy
    if flag_2cy == '是':
        info_2cy = query_2cy()
        params = {
            **params,
            'animation_type': info_2cy['animation_type'],
            'animation': ', '.join(info_2cy['animation']),
            'guoman': ', '.join(info_2cy['guoman']),
            
        }
    
    put_markdown(
        '''
        # 谢谢您的填写!
        您的姓名是：{name}, 年龄：{age}, 性别：{sex}, 当前职业：{job}。
        '''.format(**params)
    )
    if flag_2cy == "是":
        put_markdown(
            '''
            您{flag_2cy}一位二次元，
            
            最喜欢看的日漫类型是{animation_type}, 代表作有{animation}

            您喜欢的国产动漫有: {guoman}。
            
            非常开心可以认识您, 让我们一起为二次元干杯[]~(￣▽￣)~*
            '''.format(**params)
        )
    else:
        put_markdown('很遗憾您不是一位二次元呢，不过呆胶布，二次元的大门随时为您敞开~')

    lottery()
    back_home()