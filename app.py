from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h1>Котофей Матроскин</h1>
    <img src="https://rg.ru/uploads/images/212/93/18/1d222ee0-371a-11e8-bf5a-37ed9f1efa0d.jpg" />
    <p><strong>Привет, я кот <a href='https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%82_%D0%9C%D0%B0%D1%82%D1%80%D0%BE%D1%81%D0%BA%D0%B8%D0%BD'>из мультика</a>, а это моя страница</strong></p>
    <p>На ней я буду публиковать <del>свои песни и стихи</del> свой код и ссылки на <em>GitHub</em></p>
    <p>Еще тут вы сможете найти ссылки на мои рисунки, котрые я иногда делаю.</p>
    <p>Сразу <u>скажу</u> рисунки у меня так себе, <mark>потому, что у меня лапки.</mark></p>
    """
    return page_content


app.run()