# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434341846.448457
_enable_loop = True
_template_filename = u'themes/lanyon/templates/post_header.tmpl'
_template_uri = u'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_title', 'html_translations', 'html_sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        def html_title():
            return render_html_title(context)
        comments = _mako_get_namespace(context, 'comments')
        def html_translations(post):
            return render_html_translations(context,post)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <header>\n        ')
        __M_writer(unicode(html_title()))
        __M_writer(u'\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
        __M_writer(unicode(post.author()))
        __M_writer(u'</span></p>\n            <p class="dateline"><a href="')
        __M_writer(unicode(post.permalink()))
        __M_writer(u'" rel="bookmark"><time class="post-date published dt-published" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'" itemprop="datePublished" title="')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time></a></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer(u'                <p class="commentline">')
            __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer(u'\n')
        if post.description():
            __M_writer(u'                <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        __M_writer(u'        </div>\n        ')
        __M_writer(unicode(html_translations(post)))
        __M_writer(u'\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if title and not post.meta('hidetitle'):
            __M_writer(u'    <h1 class="post-title p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(post.translated_to) > 1:
            __M_writer(u'        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'</h3>\n')
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                <p><a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'" rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'">')
                    __M_writer(unicode(messages("LANGUAGE", langname)))
                    __M_writer(u'</a></p>\n')
            __M_writer(u'        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'        <p class="sourceline"><a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"131": 24, "150": 144, "138": 24, "139": 25, "140": 26, "141": 26, "142": 26, "143": 26, "144": 26, "22": 3, "25": 2, "28": 0, "33": 2, "34": 3, "35": 9, "36": 22, "37": 28, "38": 45, "44": 30, "56": 30, "57": 32, "58": 32, "59": 34, "60": 34, "61": 35, "62": 35, "63": 35, "64": 35, "65": 35, "66": 35, "67": 35, "68": 35, "69": 36, "70": 37, "71": 37, "72": 37, "73": 39, "74": 40, "75": 40, "76": 40, "77": 42, "78": 43, "79": 43, "85": 5, "91": 5, "92": 6, "93": 7, "94": 7, "95": 7, "96": 7, "97": 7, "103": 11, "111": 11, "112": 12, "113": 13, "114": 14, "115": 14, "116": 15, "117": 16, "118": 17, "119": 17, "120": 17, "121": 17, "122": 17, "123": 17, "124": 17, "125": 20}, "uri": "post_header.tmpl", "filename": "themes/lanyon/templates/post_header.tmpl"}
__M_END_METADATA
"""
