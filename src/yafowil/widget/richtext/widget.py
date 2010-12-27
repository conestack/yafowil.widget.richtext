from yafowil.base import factory
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    textarea_renderer,
)

factory.doc['widget']['richtext'] = \
"""Add-on widget `yafowil.widget.richtext 
<http://github.com/bluedynamics/yafowil.widget.richtext/>`_ .
"""

factory.defaults['richtext.default'] = ''
factory.defaults['richtext.wrap'] = None
factory.defaults['richtext.cols'] = 80
factory.defaults['richtext.rows'] = 25
factory.defaults['richtext.readonly'] = None
factory.defaults['richtext.class'] = 'richtext'
factory.register('richtext',
                 [generic_extractor, generic_required_extractor],
                 [textarea_renderer])