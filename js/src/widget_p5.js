import $ from 'jquery';

export class RichtextWidget {

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
