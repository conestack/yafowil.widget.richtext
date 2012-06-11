import os 


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [{
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