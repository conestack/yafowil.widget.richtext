import { RichtextWidget } from "../src/widget";
import $ from 'jquery';

QUnit.test('test', assert => {
    let el = $('<textarea class="richtext" />').appendTo('body');

    // mock tinymce - legacy code
    $.fn.extend({
        tinymce: function() {
            return this.each(function() {
            });
        }
    });

    RichtextWidget.initialize();
    let wid = el.data('yafowil-richtext');
    assert.ok(wid);

    // remove tinymce from jQuery namespace
    delete $.fn.tinymce;
});