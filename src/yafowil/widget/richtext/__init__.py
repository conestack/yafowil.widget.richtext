import os 

def register():
    import widget
    
def get_resource_dir(*additional):
    return os.path.join(os.path.dirname(__file__), 'resources', *additional)

def _walk_third_parties(path,postfix):
    results = []
    path_base_len = len(get_resource_dir())
    def visitor(arg, dirname, names):
        for name in names:
            if name.endswith(postfix):
                filepath = os.path.join(dirname, name).strip(os.sep)
                results.append(filepath[:path_base_len])
    os.path.walk(path, visitor,None)
    return results
        
def get_js(thirdparty=True):
    js = ['widget.js']
    #if thirdparty:
    #    target_path = os.path.join(get_resource_dir('tinymce'))
    #    js.append(_walk_third_parties(target_path,'.js'))
    return js

def get_css(thirdparty=True):
    #if not thirdparty:
    #    return []
    #target_path = os.path.join(get_resource_dir('tinymce'))
    #return _walk_third_parties(target_path,'.css')
    return []
