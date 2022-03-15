#!/bin/sh

set -e

./bin/coverage run \
    --source src/yafowil/widget/richtext \
    --omit src/yafowil/widget/richtext/example.py \
    -m yafowil.widget.richtext.tests
./bin/coverage report
./bin/coverage html
