import $ from 'jquery';

export class RichtextWidget {
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
