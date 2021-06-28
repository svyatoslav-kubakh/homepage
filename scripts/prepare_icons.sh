#!/bin/bash

CONTENT_DIRECTORY="./content"
IMAGES_DIRECTORY="${CONTENT_DIRECTORY}/images"
ICONS_DIRECTORY="${IMAGES_DIRECTORY}/icons"
EXTRA_DIRECTORY="${CONTENT_DIRECTORY}/extra"
SOURCE_IMAGE="${IMAGES_DIRECTORY}/favicon.png"

function convert_icon {
    size=$1
    target_directory=$3
    if [ -z "${target_directory}" ]
    then
        target_directory=${ICONS_DIRECTORY}
    fi
    target_file=${target_directory}/$2
    convert -verbose -resize ${size} ${SOURCE_IMAGE} ${target_file}
}

# favicon icons
convert_icon 48 "favicon.ico" ${EXTRA_DIRECTORY}
for size in 16 32 96 160 196 300
do
    convert_icon "${size}x${size}" "favicon-${size}x${size}.png"
done

# apple icons
convert_icon "180x180" "apple-touch-icon.png"
for size in 57 60 72 76 114 120 144 152 180
do
    convert_icon "${size}x${size}" "apple-touch-icon-${size}x${size}.png"
done

# mstie icons
convert_icon "144x144" "mstile-144x144.png"
convert_icon "310x150" "mstile-wide310x150.png"
for size in 70 150 310
do
    convert_icon "${size}x${size}" "mstile-square${size}x${size}.png"
done

# profile avatar
convert -verbose ${IMAGES_DIRECTORY}/profile.jpg -resize 140x140 \
    \( -size 140x140 xc:none -fill white -draw "circle 70,70 70,0" \) \
    -compose copy_opacity -composite ${ICONS_DIRECTORY}/avatar.png
