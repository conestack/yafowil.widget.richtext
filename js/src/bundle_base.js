import $ from 'jquery';

import {RichtextWidget} from './widget_base.js';

export * from './widget_base.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(RichtextWidget.initialize, true);
    } else {
        RichtextWidget.initialize();
    }
});
