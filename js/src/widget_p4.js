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
        this.id = this.elem.attr('id');
        this.config = new TinyMCEConfig(this.id);
        delete InitializedTinyMCEInstances[this.id];
        this.config.init();
    }
}
