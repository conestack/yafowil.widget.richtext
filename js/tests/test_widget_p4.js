import $ from 'jquery';
import { RichtextWidget } from '../src/widget_p4.js';

QUnit.module('RichtextWidget Plone 4', (hooks) => {
    let el, configs;

    class MockTinyMCEConfig {
        constructor(id) {
            this.id = id;
            this.initialized = 0;
            configs.push(this);
        }

        init() {
            this.initialized++;
        }
    }

    hooks.beforeEach(() => {
        configs = [];
        window.TinyMCEConfig = MockTinyMCEConfig;
        window.InitializedTinyMCEInstances = { 'input-richtext': {}, other: {} };
    });
    hooks.afterEach(() => {
        el.remove();
        delete window.TinyMCEConfig;
        delete window.InitializedTinyMCEInstances;
    });

    QUnit.test('initialize', (assert) => {
        el = $('<textarea class="richtext" id="input-richtext" />').appendTo('body');
        RichtextWidget.initialize();
        const wid = el.data('yafowil-richtext');
        assert.true(wid instanceof RichtextWidget);
        assert.true(wid.elem.is(el));
        assert.strictEqual(wid.id, 'input-richtext');
        assert.strictEqual(configs.length, 1);
        assert.strictEqual(wid.config, configs[0]);
        assert.strictEqual(wid.config.id, 'input-richtext');
        assert.strictEqual(wid.config.initialized, 1);
        assert.deepEqual(Object.keys(window.InitializedTinyMCEInstances), ['other']);
    });

    QUnit.test('initialize ignores other textareas', (assert) => {
        el = $('<textarea class="other" />').appendTo('body');
        RichtextWidget.initialize();
        assert.strictEqual(el.data('yafowil-richtext'), undefined);
        assert.strictEqual(configs.length, 0);
    });
});
