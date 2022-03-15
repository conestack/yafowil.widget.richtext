import $ from 'jquery';
import {options} from './widget_base.js';

export class RichtextWidget {

    static initialize(context) {
        $('textarea.richtext', context).each(function() {
            new RichtextWidget($(this), options);
        });
    }

    constructor(elem, options) {
        this.elem = elem;
        this.options = options;
        console.log('initialize tiny mce in plone 5 here');
    }
}
