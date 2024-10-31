import cleanup from 'rollup-plugin-cleanup';
import terser from '@rollup/plugin-terser';

const out_dir = 'src/yafowil/widget/richtext/resources';

const outro = `
window.yafowil = window.yafowil || {};
window.yafowil.richtext = exports;
`;

let versions = ['', '_p4', '_p5'];

export default args => {
    let conf = [];

    for (let ver of versions) {
        let conf_ver = {
            input: `js/src/bundle${ver}.js`,
            plugins: [
                cleanup()
            ],
            output: [{
                name: 'yafowil_richtext',
                file: `${out_dir}/widget${ver}.js`,
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
                name: 'yafowil_richtext',
                file: `${out_dir}/widget${ver}.min.js`,
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
