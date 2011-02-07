import widget
try:
    from pyramid.view import static
    tiny_mce = static('tinymce/jscripts/tiny_mce')
except ImportError:
    pass