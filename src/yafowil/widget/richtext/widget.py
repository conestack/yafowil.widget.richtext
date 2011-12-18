from yafowil.base import (
    factory,
    fetch_value,
)
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    textarea_renderer,
)


def richtext_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-richtext'})


factory.register(
    'richtext',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[textarea_renderer],
    display_renderers=[richtext_display_renderer])

factory.doc['blueprint']['richtext'] = \
"""Add-on blueprint `yafowil.widget.richtext 
<http://github.com/bluedynamics/yafowil.widget.richtext/>`_ .
"""

factory.defaults['richtext.default'] = ''

factory.defaults['richtext.wrap'] = None

factory.defaults['richtext.cols'] = 80

factory.defaults['richtext.rows'] = 25

factory.defaults['richtext.readonly'] = None

factory.defaults['richtext.class'] = 'richtext'