from yafowil.base import factory


def get_example():
    part = factory(u'fieldset', name='yafowilwidgetrichtext')
    part['richtext'] = factory('field:label:error:richtext', props={
        'label': 'TinyMCE richtext field',
        'required': 'Text is required'})
    return {'widget': part, 'routes': {}}