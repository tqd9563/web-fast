from pywebio.output import put_html, put_markdown
from cutecharts.charts import Line
# from cutecharts.components import Page
# from cutecharts.faker import Faker
from pywebio import start_server

from pyecharts import options as opts
from pyecharts.charts import Bar, Sankey
from pyecharts.faker import Faker
from libs.util import back_home

nodes = [
    {"name": "category1"},
    {"name": "category2"},
    {"name": "category3"},
    {"name": "category4"},
    {"name": "category5"},
    {"name": "category6"},
]

links = [
    {"source": "category1", "target": "category2", "value": 10},
    {"source": "category2", "target": "category3", "value": 15},
    {"source": "category3", "target": "category4", "value": 20},
    {"source": "category5", "target": "category6", "value": 25},
]

def echart_sankey():
    c = (
        Sankey()
        .add(
            "sankey",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sankey-基本示例"))
    )

    c.width = "100%"
    put_html(c.render_notebook())


def echart_barplot():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
        
    )

    c.width = "100%"
    
    put_html(c.render_notebook())

'''
export PIPENV_IGNORE_VIRTUALENVS=1
可视化
'''

def cute_lineplot() -> Line:
    chart = Line(title="Line-基本示例", width="100%")
    chart.set_options(labels=Faker.choose(), x_label="我是X轴坐标", y_label="我是Y轴坐标", legend_pos="upRight", y_tick_count=4)
    chart.add_series(name="series-A", data=Faker.values())
    chart.add_series(name="series-B", data=Faker.values())
    
    put_html(chart.render_notebook())
    

def main():
    # page = Page()
    # page.add(barplot(), lineplot())
    # put_markdown(r'''
    #     # cutecharts可视化示例
    # ''')
    # put_html(page.render_notebook())
    put_markdown(r'''
        # pyecharts可视化示例
    ''')
    put_markdown(r'''
        ## 柱状图
    ''')
    echart_barplot()

    put_markdown(r'''
        ## 桑基图
    ''')
    echart_sankey()

    put_markdown(r'''
        # cutecharts可视化示例
    ''')
    put_markdown(r'''
        ## 折线图
    ''')
    cute_lineplot()

    back_home()

# if __name__ == '__main__':
#     # start_server(main, debug=True, port=8082, auto_open_webbrowser=True)
#     start_server(main, port=8082)