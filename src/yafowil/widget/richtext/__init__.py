from yafowil.base import factory
from yafowil.utils import entry_point
import os


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'yafowil.widget.richtext.dependencies',
    'resource': 'tinymce/jscripts/tiny_mce/tiny_mce.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.richtext.jquery',
    'resource': 'tinymce/jscripts/tiny_mce/jquery.tinymce.js',
    'order': 21,
}, {
    'group': 'yafowil.widget.richtext.common',
    'resource': 'widget.js',
    'order': 22,
}]
js_plone4 = [{
    'group': 'yafowil.widget.richtext.common',
    'resource': 'widget_p4.js',
    'order': 20,
}]
js_plone5 = [{
    'group': 'yafowil.widget.richtext.common',
    'resource': 'widget_p5.js',
    'order': 20,
}]


@entry_point(order=10)
def register():
    from yafowil.widget.richtext import widget
    factory.register_theme('default', 'yafowil.widget.richtext',
                           resourcedir, js=js)
    factory.register_theme('plone4', 'yafowil.widget.richtext',
                           resourcedir, js=js_plone4)
    factory.register_theme('plone5', 'yafowil.widget.richtext',
                           resourcedir, js=js_plone5)
