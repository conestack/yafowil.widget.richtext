from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
import os
import unittest


if not IS_PY2:
    from importlib import reload


def np(path):
    return path.replace('/', os.path.sep)


class TestRichtextWidget(YafowilTestCase):

    def setUp(self):
        super(TestRichtextWidget, self).setUp()
        from yafowil.widget import richtext
        reload(richtext.widget)
        richtext.register()

    def test_edit_renderer_no_preset_value(self):
        # Render widget
        widget = factory(
            'richtext',
            name='rt',
            props={
                'required': True
            })
        self.assertEqual(widget(), (
            '<textarea class="richtext" cols="80" id="input-rt" name="rt" '
            'required="required" rows="25"></textarea>'
        ))

    def test_edit_renderer_preset_value(self):
        widget = factory(
            'richtext',
            name='rt',
            value='<p>1</p>',
            props={
                'required': True
            })
        self.assertEqual(widget(), (
            '<textarea class="richtext" cols="80" id="input-rt" name="rt" '
            'required="required" rows="25"><p>1</p></textarea>'
        ))

    def test_display_renderer(self):
        # Display renderer
        widget = factory(
            'richtext',
            name='rt',
            value='<p>foo</p>',
            mode='display')
        self.assertEqual(
            widget(),
            '<div class="display-richtext"><p>foo</p></div>'
        )

        widget = factory(
            'richtext',
            name='rt',
            mode='display')
        self.assertEqual(widget(), '<div class="display-richtext"></div>')

    def test_extraction(self):
        # Widget extraction
        widget = factory(
            'richtext',
            name='rt',
            props={
                'required': True
            })

        # Required extraction
        request = {'rt': ''}
        data = widget.extract(request)
        # No input was given
        self.assertEqual(
            data.errors,
            [ExtractionError('Mandatory field was empty')]
        )
        # Empty string in extracted
        self.assertEqual(data.extracted, '')

        # Widget extraction. Returns markup from tinymce
        request = {'rt': '<p>1</p>'}
        data = widget.extract(request)
        self.assertEqual(data.errors, [])
        self.assertEqual(data.extracted, '<p>1</p>')
        self.assertEqual(widget(data), (
            '<textarea class="richtext" cols="80" id="input-rt" name="rt" '
            'required="required" rows="25"><p>1</p></textarea>'
        ))

    def test_resources(self):
        factory.theme = 'default'
        resources = factory.get_resources('yafowil.widget.richtext')
        self.assertTrue(resources.directory.endswith(np('/richtext/resources')))
        self.assertEqual(resources.path, 'yafowil-richtext')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 3)

        self.assertTrue(scripts[0].directory.endswith(
            np('/richtext/resources/tinymce/jscripts/tiny_mce'))
        )
        self.assertEqual(
            scripts[0].path,
            'yafowil-richtext/tinymce/jscripts/tiny_mce'
        )
        self.assertEqual(scripts[0].file_name, 'tiny_mce.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(scripts[1].directory.endswith(
            np('/richtext/resources/tinymce/jscripts/tiny_mce'))
        )
        self.assertEqual(
            scripts[1].path,
            'yafowil-richtext/tinymce/jscripts/tiny_mce'
        )
        self.assertEqual(scripts[1].file_name, 'jquery.tinymce.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        self.assertTrue(scripts[2].directory.endswith(np('/richtext/resources')))
        self.assertEqual(scripts[2].path, 'yafowil-richtext')
        self.assertEqual(scripts[2].file_name, 'widget.min.js')
        self.assertTrue(os.path.exists(scripts[2].file_path))

        factory.theme = 'plone4'
        resources = factory.get_resources('yafowil.widget.richtext')
        self.assertTrue(resources.directory.endswith(np('/richtext/resources')))
        self.assertEqual(resources.path, 'yafowil-richtext')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/richtext/resources')))
        self.assertEqual(scripts[0].path, 'yafowil-richtext')
        self.assertEqual(scripts[0].file_name, 'widget_p4.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        factory.theme = 'plone5'
        resources = factory.get_resources('yafowil.widget.richtext')
        self.assertTrue(resources.directory.endswith(np('/richtext/resources')))
        self.assertEqual(resources.path, 'yafowil-richtext')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/richtext/resources')))
        self.assertEqual(scripts[0].path, 'yafowil-richtext')
        self.assertEqual(scripts[0].file_name, 'widget_p5.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))


if __name__ == '__main__':
    unittest.main()
