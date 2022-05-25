from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

default_scripts = wr.ResourceGroup(
    name='yafowil-richtext-scripts',
    path='yafowil.widget.richtext'
)
default_scripts.add(wr.ScriptResource(
    name='tinymce-js',
    directory=os.path.join(resources_dir, 'tinymce', 'jscripts', 'tiny_mce'),
    resource='tiny_mce.js',
))
default_scripts.add(wr.ScriptResource(
    name='tinymce-jquery-js',
    depends=['jquery-js', 'tinymce-js'],
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

plone4_scripts = wr.ResourceGroup(
    name='yafowil-richtext-scripts',
    path='yafowil.widget.richtext'
)
plone4_scripts.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    directory=resources_dir,
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

plone5_scripts = wr.ResourceGroup(
    name='yafowil-richtext-scripts',
    path='yafowil.widget.richtext'
)
plone5_scripts.add(wr.ScriptResource(
    name='yafowil-richtext-js',
    directory=resources_dir,
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

    # Default
    factory.register_theme(
        'default', 'yafowil.widget.richtext', resources_dir, js=default_js
    )
    factory.register_scripts(
        'default', 'yafowil.widget.richtext', default_scripts
    )

    # Plone 4
    factory.register_theme(
        'plone4', 'yafowil.widget.richtext', resources_dir, js=js_plone4
    )
    factory.register_scripts(
        'default', 'yafowil.widget.richtext', plone4_scripts
    )

    # Plone 5
    factory.register_theme(
        'plone5', 'yafowil.widget.richtext', resources_dir, js=js_plone5
    )
    factory.register_scripts(
        'default', 'yafowil.widget.richtext', plone5_scripts
    )
