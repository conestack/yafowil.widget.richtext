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
                console.log('initialize tiny mce in plone 5 here');
            }
        }
    });

})(jQuery);