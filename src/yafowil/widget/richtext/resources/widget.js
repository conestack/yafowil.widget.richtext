var yafowil_richtext = (function (exports, $) {
    'use strict';

    class RichtextWidget {
        static initialize(context) {
            let options = {
                theme: "advanced",
                plugins: "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,advlist",
                theme_advanced_buttons1: "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,|,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo",
                theme_advanced_buttons2: "tablecontrols",
                theme_advanced_buttons3: "",
                theme_advanced_toolbar_location: "top",
                theme_advanced_toolbar_align: "left",
                theme_advanced_statusbar_location: "bottom",
                theme_advanced_resizing: true
            };
            $('textarea.richtext', context).each(function() {
                new RichtextWidget($(this), options);
            });
        }
        constructor(elem, options) {
            this.elem = elem;
            this.options = options;
            this.elem.tinymce(this.options);
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
