import $ from 'jquery';

export class RichtextWidget {

    static initialize(context) {
        $('textarea.richtext', context).each(function() {
            new RichtextWidget($(this));
        });
    }

    constructor(elem) {
        this.elem = elem;
        this.id = this.elem.attr('id');
        this.config = new TinyMCEConfig(id);
        delete InitializedTinyMCEInstances[id];
        this.config.init();
    }
}
