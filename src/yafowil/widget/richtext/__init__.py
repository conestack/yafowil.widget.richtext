import os 
from yafowil.base import factory


# XXX: use fanstatic
resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'group': 'richtext',
    'resource': 'tinymce/jscripts/tiny_mce/tiny_mce.js',
    'order': 20,
}, {
    'group': 'richtext',
    'resource': 'tinymce/jscripts/tiny_mce/jquery.tinymce.js',
    'order': 21,
}, {
    'group': 'yafowil.widget.richtext',
    'resource': 'widget.js',
    'order': 22,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.richtext',
                           resourcedir, js=js)