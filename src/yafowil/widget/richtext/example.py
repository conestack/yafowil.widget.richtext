from yafowil.base import factory


DOC_RICHTEXT = """
Richtext
--------

Richtext widget using TinyMCE.

.. code-block:: python

    richtext = factory('#field:richtext', props={
        'label': 'Richtext field',
        'required': 'Text is required'})
"""

def richtext():
    part = factory(u'fieldset', name='yafowilwidgetrichtext')
    part['richtext'] = factory('#field:richtext', props={
        'label': 'Richtext field',
        'required': 'Text is required'})
    return {'widget': part,
            'doc': DOC_RICHTEXT,
            'title': 'Richtext'}


def get_example():
    return [richtext()]