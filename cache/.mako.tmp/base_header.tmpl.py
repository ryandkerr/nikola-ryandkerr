# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434512392.754425
_enable_loop = True
_template_filename = u'themes/lanyon/templates/base_header.tmpl'
_template_uri = u'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_translation_header', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <nav id="menu" role="navigation" class="sidebar-nav">\n')
        for url, text in navigation_links[lang]:
            __M_writer(u'        <a class="sidebar-nav-item" href="')
            __M_writer(unicode(url))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a>\n')
        __M_writer(u'    ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'        <div id="toptranslations">\n            <h2>')
            __M_writer(unicode(messages("Languages:")))
            __M_writer(u'</h2>\n            ')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <header id="header" role="banner">\n        ')
        __M_writer(unicode(html_site_title()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_translation_header()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_navigation_links()))
        __M_writer(u'\n')
        if search_form:
            __M_writer(u'            <div class="searchform" role="search">\n                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n            </div>\n')
        __M_writer(u'    </header>\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h3 id="brand" class="masthead-title">\n      <a href="')
        __M_writer(unicode(abs_link(_link("root", None, lang))))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'" rel="home">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n    </h3>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"133": 18, "134": 20, "135": 20, "136": 20, "137": 20, "138": 20, "139": 20, "145": 139, "22": 2, "25": 0, "32": 2, "33": 16, "34": 22, "35": 32, "36": 42, "42": 24, "51": 24, "52": 26, "53": 27, "54": 27, "55": 27, "56": 27, "57": 27, "58": 29, "59": 29, "60": 29, "61": 30, "62": 30, "68": 35, "78": 35, "79": 36, "80": 37, "81": 38, "82": 38, "83": 39, "84": 39, "90": 4, "104": 4, "105": 6, "106": 6, "107": 7, "108": 7, "109": 8, "110": 8, "111": 9, "112": 10, "113": 11, "114": 11, "115": 14, "116": 15, "117": 15, "123": 18}, "uri": "base_header.tmpl", "filename": "themes/lanyon/templates/base_header.tmpl"}
__M_END_METADATA
"""
