# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1435629633.646256
_enable_loop = True
_template_filename = u'/home/ryan/.virtualenvs/nikola-web/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        description = context.get('description', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(unicode(title)))
        __M_writer(u'</h1>\n')
        if description:
            __M_writer(u'        <p>')
            __M_writer(unicode(description))
            __M_writer(u'</p>\n')
        if subcategories:
            __M_writer(u'        ')
            __M_writer(unicode(messages('Subcategories:')))
            __M_writer(u'\n        <ul>\n')
            for name, link in subcategories:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(name))
                __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        __M_writer(u'        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer(u'                <p class="feedlink">\n                    <a href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'" hreflang="')
                __M_writer(unicode(language))
                __M_writer(u'" type="application/rss+xml">')
                __M_writer(unicode(messages('RSS feed', language)))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer(u'                <p class="feedlink"><a href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'" type="application/rss+xml">')
            __M_writer(unicode(messages('RSS feed')))
            __M_writer(u'</a></p>\n')
        __M_writer(u'        </div>\n    </header>\n')
        if posts:
            __M_writer(u'    <ul class="postlist">\n')
            for post in posts:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(post.permalink()))
                __M_writer(u'" class="listtitle">')
                __M_writer(filters.html_escape(unicode(post.title())))
                __M_writer(u'</a> <time class="listdate" datetime="')
                __M_writer(unicode(post.date.isoformat()))
                __M_writer(u'" title="')
                __M_writer(unicode(post.formatted_date(date_format)))
                __M_writer(u'">')
                __M_writer(unicode(post.formatted_date(date_format)))
                __M_writer(u'</time></li>\n')
            __M_writer(u'    </ul>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(unicode(kind))
                __M_writer(u' ')
                __M_writer(unicode(tag))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">\n')
        elif generate_rss:
            __M_writer(u'        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(unicode(kind))
            __M_writer(u' ')
            __M_writer(unicode(tag))
            __M_writer(u'" href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 46, "129": 46, "130": 46, "131": 46, "132": 46, "133": 48, "134": 50, "140": 4, "153": 4, "26": 0, "155": 5, "156": 6, "154": 5, "158": 8, "159": 8, "160": 8, "161": 8, "162": 8, "163": 8, "164": 8, "165": 8, "166": 8, "167": 10, "168": 11, "169": 11, "170": 11, "171": 11, "172": 11, "173": 11, "174": 11, "157": 7, "48": 2, "180": 174, "53": 13, "58": 51, "64": 16, "82": 16, "83": 19, "84": 19, "85": 20, "86": 21, "87": 21, "88": 21, "89": 23, "90": 24, "91": 24, "92": 24, "93": 26, "94": 27, "95": 27, "96": 27, "97": 27, "98": 27, "99": 29, "100": 31, "101": 32, "102": 33, "103": 34, "104": 35, "105": 35, "106": 35, "107": 35, "108": 35, "109": 35, "110": 35, "111": 35, "112": 38, "113": 39, "114": 39, "115": 39, "116": 39, "117": 39, "118": 41, "119": 43, "120": 44, "121": 45, "122": 46, "123": 46, "124": 46, "125": 46, "126": 46, "127": 46}, "uri": "tag.tmpl", "filename": "/home/ryan/.virtualenvs/nikola-web/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl"}
__M_END_METADATA
"""
