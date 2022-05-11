import { RichtextWidget } from "../src/widget";

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
    let wid = el.data('richtext');
    assert.ok(wid);

    // remove tinymce from jQuery namespace
    delete $.fn.tinymce;
});