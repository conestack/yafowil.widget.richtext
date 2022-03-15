var yafowil_richtext_p5 = (function (exports, $) {
    'use strict';

    class RichtextWidget {
        static initialize(context) {
            $('textarea.richtext', context).each(function() {
                new RichtextWidget($(this));
            });
        }
        constructor(elem) {
            this.elem = elem;
            console.log('initialize tiny mce in plone 5 here');
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
