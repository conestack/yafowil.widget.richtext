import $ from 'jquery';

import {RichtextWidget} from './widget_p5.js';

export * from './widget_p5.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(RichtextWidget.initialize, true);
    } else {
        RichtextWidget.initialize();
    }
});
