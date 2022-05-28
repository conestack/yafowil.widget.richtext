from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

default_resources = wr.ResourceGroup(
    name='yafowil-richtext-resources',
    directory=resources_dir,
    path='yafowil-richtext'
)
default_resources.add(wr.ScriptResource(
    name='tinymce-js',
    directory=os.path.join(resources_dir, 'tinymce', 'jscripts', 'tiny_mce'),
    path='yafowil-richtext/tinymce/jscripts/tiny_mce',
    resource='tiny_mce.js',
))
default_resources.add(wr.ScriptResource(
    name='tinymce-jquery-js',
    depends=['jquery-js', 'tinymce-js'],
    directory=os.path.join(resources_dir, 'tinymce', 'jscripts', 'tiny_mce'),
    path='yafowil-richtext/tinymce/jscripts/tiny_mce',
    resource='jquery.tiny_mce.js',
))
default_resources.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    depends='tinymce-jquery-js',
    resource='widget.js',
    compressed='widget.min.js'
))

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

plone4_resources = wr.ResourceGroup(
    name='yafowil-richtext-resources',
    directory=resources_dir,
    path='yafowil-richtext'
)
plone4_resources.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    resource='widget_p4.js',
    compressed='widget_p4.min.js'
))

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

plone5_resources = wr.ResourceGroup(
    name='yafowil-richtext-resources',
    directory=resources_dir,
    path='yafowil-richtext'
)
plone5_resources.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    resource='widget_p5.js',
    compressed='widget_p5.min.js'
))

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

    widget_name = 'yafowil.widget.richtext'

    # Default
    factory.register_theme('default', widget_name, resources_dir, js=default_js)
    factory.register_resources('default', widget_name, default_resources)

    # Plone 4
    factory.register_theme('plone4', widget_name, resources_dir, js=js_plone4)
    factory.register_resources('default', widget_name, plone4_resources)

    # Plone 5
    factory.register_theme('plone5', widget_name, resources_dir, js=js_plone5)
    factory.register_resources('default', widget_name, plone5_resources)
