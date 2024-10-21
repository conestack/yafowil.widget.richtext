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

    <div class="alert alert-info">
        <i class="bi bi-info-circle-fill"></i>
        This widget has a newer version available:
        <a class="link-offset-3"
           href="../++widget++yafowil.widget.tiptap/index.html">
            yafowil.widget.tiptap
        </a>
    </div>
    <div class="alert alert-warning">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Deprecation Notice:</strong>
        yafowil.widget.richtext is 
        <strong>
            deprecated
        </strong>
        and will no longer receive support or further development.
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
