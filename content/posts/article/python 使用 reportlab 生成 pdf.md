---
title: python 使用 reportlab 生成 pdf
date: 2022-02-09T15:30:51+08:00
categories: [csdn]
---

> https://blog.csdn.net/wolanx/article/details/122828185

## Intro
项目中遇到需要 `导出统计报表` 等业务时，通常需要 `pdf` 格式。`python` 中比较有名的就是 `reportlab` 。
这边通过几个小 demo 快速演示常用 api。所有功能点 `源码` 都在 `使用场景`。

> 一句话了解：跟 css 差不多，就是不断地对每样东西设置 style，然后把 style 和内容绑定。

## 功能点
- 生成
  - 文件： 先 SimpleDocTemplate('xxx.pdf')，然后 build
  - 流文件：先 io.BytesIO() 生成句柄，然后同理
- 曲线图 `LinePlot`
- 饼图 `Pie`
- 文字 `Paragraph`
  - fontSize 字体大小 推荐 14
  - 加粗 `<b>xxx</b>` 使用的是 html 的方式，字体自动实现
  - firstLineIndent 首行缩进 推荐 2 * fontSize
  - leading 行间距 推荐 1.5 * fontSize
  - fontName 默认中文会变成 ■
    - 下载 .ttf 文件 至少2个 【常规】【加粗】
    - 注册字体 pdfmetrics.registerFont 【常规】请用原名，方便加粗的实现
    - 注册字体库 registerFontFamily("HanSans", normal="HanSans", bold="HanSans-Bold")

> 其他 api 自行摸索，但基本离不开 css 那种理念。官网并没有常规文档的那种 md 模式，而是完全写在了 pdf 里，玩家需要自己去 pdf 里像查字典一样去找。[官方文档](https://www.reportlab.com/docs/reportlab-userguide.pdf)

## 预览
![在这里插入图片描述](https://img-blog.csdnimg.cn/96e96089aad744db917372a1a1770785.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAeXVqaWUuemhhbw==,size_12,color_FFFFFF,t_70,g_se,x_16#pic_center)
## 完整代码
```python
import os

from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

home = os.path.expanduser("~")

try:
    pdfmetrics.registerFont(TTFont("HanSans", f"{home}/.fonts/SourceHanSansCN-Normal.ttf"))
    pdfmetrics.registerFont(TTFont("HanSans-Bold", f"{home}/.fonts/SourceHanSansCN-Bold.ttf"))
    registerFontFamily("HanSans", normal="HanSans", bold="HanSans-Bold")
    FONT_NAME = "HanSans"
except:
    FONT_NAME = "Helvetica"


class MyCSS:
    h3 = ParagraphStyle(name="h3", fontName=FONT_NAME, fontSize=14, leading=21, alignment=1)
    p = ParagraphStyle(name="p", fontName=FONT_NAME, fontSize=12, leading=18, firstLineIndent=24)


class PiiPdf:
    @classmethod
    def doH3(cls, text: str):
        return Paragraph(text, MyCSS.h3)

    @classmethod
    def doP(cls, text: str):
        return Paragraph(text, MyCSS.p)

    @classmethod
    def doLine(cls):
        drawing = Drawing(500, 220)
        line = LinePlot()
        line.x = 50
        line.y = 50
        line.height = 125
        line.width = 300
        line.lines[0].strokeColor = colors.blue
        line.lines[1].strokeColor = colors.red
        line.lines[2].strokeColor = colors.green
        line.data = [((0, 50), (100, 100), (200, 200), (250, 210), (300, 300), (400, 800))]

        drawing.add(line)
        return drawing

    @classmethod
    def doChart(cls, data):
        drawing = Drawing(width=500, height=200)
        pie = Pie()
        pie.x = 150
        pie.y = 65
        pie.sideLabels = False
        pie.labels = [letter for letter in "abcdefg"]
        pie.data = data  # list(range(15, 105, 15))
        pie.slices.strokeWidth = 0.5

        drawing.add(pie)
        return drawing
```

## 使用场景1：生成文件
```bash
doc = SimpleDocTemplate("Hello.pdf")

p = PiiPdf()
doc.build([
    p.doH3("<b>水泵能源消耗简报</b>"),
    p.doH3("<b>2021.12.1 ~ 2021.12.31</b>"),
    p.doP("该月接入能耗管理系统水泵系统 xx 套，水泵 x 台。"),
    p.doP("本月最大总功率 xx kW，环比上月增加 xx %，平均功率 xx kW；环比上月增加 xx %。"),
    p.doP("功率消耗趋势图："),
    p.doLine(),
    p.doP("本月总能耗 xxx kWh，环比上月增加 xx %。"),
    p.doP("分水泵能耗统计："),
    p.doChart(list(range(15, 105, 20))),
    p.doP("其中能耗最高的水泵为：xxx， 环比上月增加 xxx kWh，xx %。"),
])
```

## 使用场景2：web（flask）
```python
@Controller.get("/api/pdf")
def api_hub_energy_pdf():
    buffer = io.BytesIO()										# 重点 起一个 io
    doc = SimpleDocTemplate(buffer)

    p = PiiPdf()
    doc.build([
        p.doH3("<b>2021.12.1 ~ 2021.12.31</b>"),
    ])

    buffer.seek(0)
    return Response(											# io 形式返回
        buffer,
        mimetype="application/pdf",
        headers={"Content-disposition": "inline; filename=test.pdf"},
    )
```
