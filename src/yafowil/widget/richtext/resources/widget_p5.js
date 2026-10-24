var yafowil_richtext = (function (exports, $) {
    'use strict';

    class RichtextWidget {
        static initialize(context) {
            $('textarea.richtext', context).each(function () {
                new RichtextWidget($(this));
            });
        }
        constructor(elem) {
            elem.data('yafowil-richtext', this);
            this.elem = elem;
            mockup_require(['mockup-patterns-tinymce'], (tinymce) => {
                $.ajax('@@yafowil.tinymce.options', {
                    dataType: 'json',
                    success: (data) => {
                        new tinymce(elem, data);
                    },
                    error: () => {
                        console.log(
                            'Failed to fetch TinyMCE Options. ' + 'Initialize with default options',
                        );
                        new tinymce(elem, {});
                    },
                });
            });
        }
    }

    $(() => {
        if (window.ts !== undefined) {
            ts.ajax.register(RichtextWidget.initialize, true);
        } else if (window.bdajax !== undefined) {
            bdajax.register(RichtextWidget.initialize, true);
        } else {
            RichtextWidget.initialize();
        }
    });

    exports.RichtextWidget = RichtextWidget;

    Object.defineProperty(exports, '__esModule', { value: true });


    window.yafowil = window.yafowil || {};
    window.yafowil.richtext = exports;


    return exports;

})({}, jQuery);
