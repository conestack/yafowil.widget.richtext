from node.utils import UNSET
from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
from yafowil.tests import fxml
import yafowil.loader


if not IS_PY2:
    from importlib import reload


class TestRichtextWidget(YafowilTestCase):

    def setUp(self):
        super(TestRichtextWidget, self).setUp()
        from yafowil.widget.richtext import widget
        reload(widget)

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
        self.assertEqual(widget(),
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


if __name__ == '__main__':
    unittest.main()                                          # pragma: no cover
