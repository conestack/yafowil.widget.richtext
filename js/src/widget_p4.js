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
        this.id = this.elem.attr('id');
        this.config = new TinyMCEConfig(id);
        delete InitializedTinyMCEInstances[id];
        this.config.init();
    }
}
