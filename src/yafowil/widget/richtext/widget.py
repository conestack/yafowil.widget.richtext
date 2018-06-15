from yafowil.base import factory
from yafowil.base import fetch_value
from yafowil.common import generic_extractor
from yafowil.common import generic_required_extractor
from yafowil.common import textarea_renderer
from yafowil.utils import attr_value
from yafowil.utils import cssid
from yafowil.utils import generic_html5_attrs


def richtext_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-richtext'})


def richtext_edit_renderer(widget, data):
    rendered = textarea_renderer(widget, data)
    optiontags = []
    mimetypes = attr_value('mimetypes', widget, data)
    if not 'text/html' in mimetypes:
        raise Exception('"text/html" not contained in mimetypes')
    if len(mimetypes) == 1:
        return rendered
    for mimetype in mimetypes:
        optiontags.append(data.tag('option', mimetype))
    select_attrs = {
        'name_': '{}.mimetype'.format(widget.dottedpath),
        'id': cssid(widget, 'input.mimetype'),
        'class': attr_value('mimetypes_class', widget, data)
    }
    mimetypes_data = attr_value('mimetypes_data', widget, data)
    select_attrs.update(generic_html5_attrs(mimetypes_data))
    rendered += data.tag('select', *optiontags, **select_attrs)
    return rendered


factory.register(
    'richtext',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[richtext_edit_renderer],
    display_renderers=[richtext_display_renderer])

factory.doc['blueprint']['richtext'] = \
"""Add-on blueprint `yafowil.widget.richtext 
<http://github.com/bluedynamics/yafowil.widget.richtext/>`_ .
"""

factory.defaults['richtext.default'] = ''

factory.defaults['richtext.wrap'] = None
factory.doc['props']['richtext.wrap'] = \
"""Either ``soft``, ``hard``, ``virtual``, ``physical`` or  ``off``.
"""

factory.defaults['richtext.cols'] = 80
factory.doc['props']['richtext.cols'] = \
"""Number of characters.
"""

factory.defaults['richtext.rows'] = 25
factory.doc['props']['richtext.rows'] = \
"""Number of lines.
"""

factory.defaults['richtext.readonly'] = None
factory.doc['props']['richtext.readonly'] = \
"""Flag for readonly.
"""

factory.defaults['richtext.mimetypes'] = ['text/html']
factory.doc['props']['richtext.mimetypes'] = \
"""List of mimetypes.
"""

factory.defaults['richtext.mimetypes_class'] = ''
factory.doc['props']['richtext.mimetypes_class'] = \
"""CSS class to be set on mimetypes selection.
"""

factory.defaults['richtext.mimetypes_data'] = {}
factory.doc['props']['richtext.mimetypes_data'] = \
"""Dict containing data attributes to render on mimetypes selection.
"""

factory.defaults['richtext.class'] = 'richtext'
