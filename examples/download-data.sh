#!/bin/bash

set -e

echo "Downloading data..."
wget -P examples-utils/ https://www.dropbox.com/sh/bzdn4psttd2ehov/AAAlZP294vIFaj5JXXPEX1_Ia/examples-utils.zip
echo "Unzipping data..."
pushd examples-utils
unzip examples-utils.zip
rm examples-utils.zip
popd
echo "Done!"
