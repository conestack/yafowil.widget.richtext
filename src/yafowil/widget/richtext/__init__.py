from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

default_scripts = wr.ResourceGroup(name='scripts')
default_scripts.add(wr.ScriptResource(
    name='tinymce-js',
    # actually it not depends on jquery, but tinymce-jquery-js does
    # think about multiple depends values in webresource
    depends='jquery-js',
    directory=os.path.join(resources_dir, 'tinymce', 'jscripts', 'tiny_mce'),
    resource='tiny_mce.js',
))
default_scripts.add(wr.ScriptResource(
    name='tinymce-jquery-js',
    depends='tinymce-js',
    directory=os.path.join(resources_dir, 'tinymce', 'jscripts', 'tiny_mce'),
    resource='jquery.tiny_mce.js',
))
default_scripts.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    depends='tinymce-jquery-js',
    directory=resources_dir,
    resource='widget.js',
    compressed='widget.min.js'
))

default_resources = wr.ResourceGroup(name='richtext-resources')
default_resources.add(default_scripts)

# B/C resources ##############################################################

default_js = [{
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


##############################################################################
# Plone 4
##############################################################################

# webresource ################################################################

plone4_scripts = wr.ResourceGroup(name='scripts')
plone4_scripts.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    directory=resources_dir,
    resource='widget_p4.js',
    compressed='widget_p4.min.js'
))

plone4_resources = wr.ResourceGroup(name='richtext-resources')
plone4_resources.add(plone4_scripts)

# B/C resources ##############################################################

js_plone4 = [{
    'group': 'yafowil.widget.richtext.common',
    'resource': 'widget_p4.js',
    'order': 20,
}]


##############################################################################
# Plone 5
##############################################################################

# webresource ################################################################

plone5_scripts = wr.ResourceGroup(name='scripts')
plone5_scripts.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    directory=resources_dir,
    resource='widget_p5.js',
    compressed='widget_p5.min.js'
))

plone5_resources = wr.ResourceGroup(name='richtext-resources')
plone5_resources.add(plone5_scripts)

# B/C resources ##############################################################

js_plone5 = [{
    'group': 'yafowil.widget.richtext.common',
    'resource': 'widget_p5.js',
    'order': 20,
}]


##############################################################################
# Registration
##############################################################################

@entry_point(order=10)
def register():
    from yafowil.widget.richtext import widget  # noqa

    # Default
    factory.register_theme(
        'default', 'yafowil.widget.richtext', resources_dir,
        js=default_js, resources=default_resources
    )
    # Plone 4
    factory.register_theme(
        'plone4', 'yafowil.widget.richtext', resources_dir,
        js=js_plone4, resources=plone4_resources
    )
    # Plone 5
    factory.register_theme(
        'plone5', 'yafowil.widget.richtext', resources_dir,
        js=js_plone5, resources=plone5_resources
    )
