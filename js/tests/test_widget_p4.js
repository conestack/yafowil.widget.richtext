import $ from 'jquery';
import { RichtextWidget } from '../src/widget_p4.js';

QUnit.module('RichtextWidget Plone 4', () => {
    QUnit.test('initialize ignores other textareas', (assert) => {
        const el = $('<textarea class="other" />').appendTo('body');
        RichtextWidget.initialize();
        assert.strictEqual(el.data('yafowil-richtext'), undefined);
        el.remove();
    });
});
