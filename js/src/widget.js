import $ from 'jquery';

export class RichtextWidget {

    static initialize(context) {
        // tinymce options. extend or override as desired
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
