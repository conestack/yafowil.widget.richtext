import $ from 'jquery';
import { RichtextWidget } from '../src/widget';

QUnit.test('test', (assert) => {
    const el = $('<textarea class="richtext" />').appendTo('body');

    // mock tinymce - legacy code
    $.fn.extend({
        tinymce: function () {
            return this.each(() => {});
        },
    });

    RichtextWidget.initialize();
    const wid = el.data('yafowil-richtext');
    assert.ok(wid);

    // remove tinymce from jQuery namespace
    delete $.fn.tinymce;
});
