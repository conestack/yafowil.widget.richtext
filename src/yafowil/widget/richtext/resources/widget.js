/* 
 * yafowil richtext widget
 * 
 * Requires: tinymce
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.richtext.binder();
        
        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                richtext_binder: yafowil.richtext.binder
            });
        }
    });
    
    $.extend(yafowil, {
        
        richtext: {
            
            // tinymce options. extend or override as desired
            options: {
                script_url: '/tiny_mce/tiny_mce.js',
                theme: "advanced",
                plugins: "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,advlist",
                theme_advanced_buttons1: "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,|,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo",
                theme_advanced_buttons2: "tablecontrols",
                theme_advanced_buttons3: "",
                theme_advanced_toolbar_location: "top",
                theme_advanced_toolbar_align: "left",
                theme_advanced_statusbar_location: "bottom",
                theme_advanced_resizing: true
            },
            
            binder: function(context) {
                $('textarea.richtext', context)
                    .tinymce(yafowil.richtext.options);
            }
        }
    });

})(jQuery);