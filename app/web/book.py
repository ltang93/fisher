from flask import jsonify, request
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
            q:普通关键字 isbn
            page
    """
    # Request Response
    # HTTP 的请求信息
    # 查询参数 POST参数 remote ip
    # q = request.args['q']
    # #至少1个字符，长度限制
    # page = request.args['page'] #不可变的dict ; 转换为可变：a=request.args.to_dict()
    # 正整数，长度限制

    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        # 验证通过
        q = form.q.data.strip() #strip去除前后空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
        # return json.dumps(result),200,{'content-type':'application/json'}
    else:
        return jsonify(form.errors)
