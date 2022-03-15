import $ from 'jquery';

export class RichtextWidget {

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
