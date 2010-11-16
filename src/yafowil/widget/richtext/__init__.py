import widget
try:
    from repoze.bfg.view import static
    tiny_mce = static('tinymce/jscripts/tiny_mce')
except ImportError:
    pass