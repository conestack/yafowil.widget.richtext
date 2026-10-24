import $ from 'jquery';
import { RichtextWidget } from '../src/widget_p5.js';

QUnit.module('RichtextWidget Plone 5', (hooks) => {
    const orig_ajax = $.ajax;
    const orig_log = console.log;
    let el, created, required, ajax_calls, logged;

    function last_created() {
        return created[created.length - 1];
    }

    class MockTinyMCE {
        constructor(elem, options) {
            created.push([elem, options]);
        }
    }

    hooks.beforeEach(() => {
        el = $('<textarea class="richtext" />').appendTo('body');
        created = [];
        required = [];
        ajax_calls = [];
        logged = [];
        window.mockup_require = (deps, callback) => {
            required.push(deps);
            callback(MockTinyMCE);
        };
        $.ajax = (url, settings) => {
            ajax_calls.push([url, settings]);
        };
        console.log = (msg) => {
            logged.push(msg);
        };
    });
    hooks.afterEach(() => {
        el.remove();
        $.ajax = orig_ajax;
        console.log = orig_log;
        delete window.mockup_require;
    });

    QUnit.test('initialize with fetched options', (assert) => {
        RichtextWidget.initialize();
        const wid = el.data('yafowil-richtext');
        assert.true(wid instanceof RichtextWidget);
        assert.true(wid.elem.is(el));
        assert.deepEqual(required, [['mockup-patterns-tinymce']]);
        assert.strictEqual(ajax_calls.length, 1);
        const [url, settings] = ajax_calls[0];
        assert.strictEqual(url, '@@yafowil.tinymce.options');
        assert.strictEqual(settings.dataType, 'json');

        assert.strictEqual(created.length, 0);

        const options = { plugins: 'table' };
        settings.success(options);
        assert.strictEqual(created.length, 1);
        assert.true(last_created()[0].is(el));
        assert.strictEqual(last_created()[1], options);
        assert.deepEqual(logged, []);
    });

    QUnit.test('initialize with default options if fetching fails', (assert) => {
        RichtextWidget.initialize();
        assert.true(el.data('yafowil-richtext') instanceof RichtextWidget);
        assert.strictEqual(ajax_calls.length, 1);
        assert.strictEqual(created.length, 0);

        ajax_calls[0][1].error();
        assert.strictEqual(created.length, 1);
        assert.true(last_created()[0].is(el));
        assert.deepEqual(last_created()[1], {});
        assert.deepEqual(logged, [
            'Failed to fetch TinyMCE Options. Initialize with default options',
        ]);
    });
});
