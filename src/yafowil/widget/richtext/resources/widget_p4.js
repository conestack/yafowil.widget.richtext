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

            binder: function(context) {
                $('textarea.richtext', context).each(function() {
                    var id = $(this).attr('id');
                    var config = new TinyMCEConfig(id);
                    delete InitializedTinyMCEInstances[id];
                    config.init();
                });
            }
        }
    });

})(jQuery);
