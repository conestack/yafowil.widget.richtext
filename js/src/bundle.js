import $ from 'jquery';

import {RichtextWidget} from './widget.js';

export * from './widget.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(RichtextWidget.initialize, true);
    } else {
        RichtextWidget.initialize();
    }
});
