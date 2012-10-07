import os 
from yafowil.base import factory


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


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.richtext',
                           resourcedir, js=js)