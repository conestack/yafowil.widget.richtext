import os 
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'resource': 'tinymce/jscripts/tiny_mce/tiny_mce.js',
    'thirdparty': True,
    'order': 20,
}, {
    'resource': 'tinymce/jscripts/tiny_mce/jquery.tinymce.js',
    'thirdparty': False,
    'order': 21,
}, {
    'resource': 'widget.js',
    'thirdparty': False,
    'order': 22,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.richtext',
                           resourcedir, js=js)