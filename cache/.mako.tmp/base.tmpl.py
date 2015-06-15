# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434341846.310375
_enable_loop = True
_template_filename = u'themes/lanyon/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'header', context._clean_inheritance_tokens(), templateuri=u'base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'header')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    ns = runtime.TemplateNamespace(u'annotations', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'annotations')] = ns

    ns = runtime.TemplateNamespace(u'footer', context._clean_inheritance_tokens(), templateuri=u'base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _mako_get_namespace(context, 'header')
        base = _mako_get_namespace(context, 'base')
        lanyon_subtheme = _import_ns.get('lanyon_subtheme', context.get('lanyon_subtheme', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n')
        if lanyon_subtheme:
            __M_writer(u'<body class="')
            __M_writer(unicode(lanyon_subtheme))
            __M_writer(u'">\n')
        else:
            __M_writer(u'<body>\n')
        __M_writer(u'    <a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(unicode(messages("Skip to main content")))
        __M_writer(u'</a>\n    <!-- Target for toggling the sidebar `.sidebar-checkbox` is for regular\n            styles, `#sidebar-checkbox` for behavior. -->\n    <input type="checkbox" class="sidebar-checkbox" id="sidebar-checkbox">\n\n    <!-- Toggleable sidebar -->\n    <div class="sidebar" id="sidebar">\n        <div class="sidebar-item">\n            <img class="circular" src="../img/ryan_propic1.jpg">\n            <p>The personal blog and portfolio of <a href="stories/about.html">Ryan Kerr</a>. Musings on programming, data, visualization and life.</p> \n\n            <!-- <p>A reserved <a href="http://getnikola.com" target="_blank">Nikola</a> theme that places the utmost gravity on content with a hidden drawer. Made by <a href="https://twitter.com/mdo" target="_blank">@mdo</a> for Jekyll,\n            ported to Nikola by <a href="https://twitter.com/ralsina" target="_blank">@ralsina</a>.</p> -->\n        </div>\n        ')
        __M_writer(unicode(header.html_navigation_links()))
        __M_writer(u'\n    </div>\n\n    <!-- Wrap is the content to shift when toggling the sidebar. We wrap the\n         content to avoid any CSS collisions with our real content. -->\n    <div class="wrap">\n      <div class="masthead">\n        <div class="container">\n          ')
        __M_writer(unicode(header.html_site_title()))
        __M_writer(u'\n        </div>\n      </div>\n\n      <div class="container content" id="content">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n        ')
        __M_writer(unicode(footer.html_footer()))
        __M_writer(u'\n      </div>\n    </div>\n    <label for="sidebar-checkbox" class="sidebar-toggle"></label>\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"134": 8, "140": 53, "22": 3, "25": 2, "155": 140, "28": 5, "31": 4, "34": 0, "58": 2, "59": 3, "60": 4, "61": 5, "62": 6, "63": 6, "64": 7, "65": 7, "70": 10, "71": 11, "72": 11, "73": 13, "74": 14, "75": 14, "76": 14, "77": 15, "78": 16, "79": 18, "80": 18, "81": 18, "82": 32, "83": 32, "84": 40, "85": 40, "90": 45, "91": 46, "92": 46, "93": 50, "94": 50, "95": 51, "96": 51, "97": 52, "98": 52, "103": 53, "109": 45, "124": 8}, "uri": "base.tmpl", "filename": "themes/lanyon/templates/base.tmpl"}
__M_END_METADATA
"""
