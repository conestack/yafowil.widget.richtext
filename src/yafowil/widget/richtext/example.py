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


DOC_RICHTEXT_DEPRECATION = """
.. raw:: html

    <div class="alert alert-danger">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Deprecation Notice:</strong>
        yafowil.widget.richtext is 
        <strong>
            deprecated
        </strong>
        and will no longer receive support or further development.
        Please use 
        <a class="link-offset-3"
           href="../++widget++yafowil.widget.tiptap/index.html">
            yafowil.widget.tiptap
        </a>
        instead.
    </div>
"""


def richtext():
    part = factory(u'fieldset', name='yafowilwidgetrichtext')
    part['richtext'] = factory('#field:richtext', props={
        'label': 'Richtext field',
        'required': 'Text is required'})
    return {
        'widget': part,
        'doc': DOC_RICHTEXT if factory.theme != 'bootstrap5'
               else DOC_RICHTEXT_DEPRECATION + DOC_RICHTEXT,
        'title': 'Richtext'
    }


def get_example():
    return [richtext()]
