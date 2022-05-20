var yafowil_richtext_p5 = (function (exports, $) {
    'use strict';

    class RichtextWidget {
        static initialize(context) {
            $('textarea.richtext', context).each(function() {
                new RichtextWidget($(this));
            });
        }
        constructor(elem) {
            elem.data('yafowil-richtext', this);
            this.elem = elem;
            mockup_require(['mockup-patterns-tinymce'], function(tinymce) {
                $.ajax('@@yafowil.tinymce.options', {
                    dataType: 'json',
                    success: function(data, status, request) {
                        new tinymce(elem, data);
                    },
                    error: function(request, status, error) {
                        console.log(
                            'Failed to fetch TinyMCE Options. ' +
                            'Initialize with default options'
                        );
                        new tinymce(elem, {});
                    }
                });
                new tinymce(elem, {});
            });
        }
    }

    $(function() {
        if (window.ts !== undefined) {
            ts.ajax.register(RichtextWidget.initialize, true);
        } else {
            RichtextWidget.initialize();
        }
    });

    exports.RichtextWidget = RichtextWidget;

    Object.defineProperty(exports, '__esModule', { value: true });


    if (window.yafowil === undefined) {
        window.yafowil = {};
    }

    window.yafowil.richtext = exports;


    return exports;

})({}, jQuery);
