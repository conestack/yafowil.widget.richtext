import cleanup from 'rollup-plugin-cleanup';
import {terser} from 'rollup-plugin-terser';

const out_dir = 'src/yafowil/widget/richtext/resources';

const outro = `
if (window.yafowil === undefined) {
    window.yafowil = {};
}

window.yafowil.richtext = exports;
`;

let versions = ['base', 'p4', 'p5'];

export default args => {
    let conf = [];

    for (let ver of versions) {
        let conf_ver = {
            input: `js/src/bundle_${ver}.js`,
            plugins: [
                cleanup()
            ],
            output: [{
                name: `yafowil_richtext_${ver}`,
                file: `${out_dir}/widget_${ver}.js`,
                format: 'iife',
                outro: outro,
                globals: {
                    jquery: 'jQuery'
                },
                interop: 'default'
            }],
            external: [
                'jquery'
            ]
        };
        if (args.configDebug !== true) {
            conf_ver.output.push({
                name: `yafowil_richtext_${ver}`,
                file: `${out_dir}/widget_${ver}.min.js`,
                format: 'iife',
                plugins: [
                    terser()
                ],
                outro: outro,
                globals: {
                    jquery: 'jQuery'
                },
                interop: 'default'
            });
        }
        conf.push(conf_ver);
    }
    return conf;
};
