# Convert File Format

This program convers the file format.

## Support

- svg -> png
- mp4 -> gif
- png -> ico
- png -> svg
- mp4(H.265) -> mp4(H.264)
- img(s) -> gif

## Prepare

```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec --user $UID convert_file_format bash
$ cd /work
```

### About ``libssl1``

``libssl1.0.0`` get from http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/ .  
``docker-compose build`` may be failed by the version up.  
If nessesary, please update link in ``docker/Dockerfile``.

## Usage

```
$ python3 convert_file_format.py --help
usage: convert_file_format.py [-h] --convert_type {svg2png,mp42gif,png2ico,png2svg} --input_file INPUT_FILE
                              --output_file OUTPUT_FILE

Convert file format

options:
  -h, --help            show this help message and exit
  --convert_type {svg2png,mp42gif,png2ico,png2svg}
                        convert type
  --input_file INPUT_FILE
                        input file path
  --output_file OUTPUT_FILE
                        output file path
```

### SVG2PNG

```
$ python3 convert_file_format.py --convert_type svg2png --input_file <input_file> --output_file <output_file>
```

#### Output sample of ``./sample_data/svg/directory_structure.svg``

![directory_structure.png](./images/directory_structure.png)

### MP42GIF

```
$ python3 convert_file_format.py --convert_type mp42gif --input_file <input_file> --output_file <output_file>
```

#### Output sample of ``./sample_data/mp4/run_svg2png.mp4``
![run_svg2png.gif](./images/run_svg2png.gif)


### PNG2ICO

```
$ python3 convert_file_format.py --convert_type png2ico --input_file <input_file> --output_file <output_file>
```


### PNG2SVG

```
$ python3 convert_file_format.py --convert_type png2svg --input_file <input_file> --output_file <output_file>
```

### MP4 (H.265->H.264)

```
$ python3 convert_file_format.py --convert_type mp4_h265toh264 --input_file <input_file> --output_file <output_file>
```

### Image files to GIF

```
$ python3 convert_file_format.py --convert_type imgs2gif --input_file <input directory path> --output_file <output_file>
```

#### Output sample of ``./sample_data/png/light_shifted_images``
![run_imgs2gif](./images/run_imgs2gif.gif)

## Modules and Licenses

```
$ pip-licenses
 Name                           Version     License
 Babel                          2.14.0      BSD License
 Jinja2                         3.1.3       BSD License
 MarkupSafe                     2.1.4       BSD License
 Pillow                         10.0.0      Historical Permission Notice and Disclaimer (HPND)
 PyGObject                      3.42.1      GNU Lesser General Public License v2 or later (LGPLv2+)
 Pygments                       2.17.2      BSD License
 Sphinx                         7.0.0       BSD License
 alabaster                      0.7.16      BSD License
 aspose-words                   23.6.0      Free To Use But Restricted; Other/Proprietary License
 certifi                        2023.11.17  Mozilla Public License 2.0 (MPL 2.0)
 chardet                        5.2.0       GNU Lesser General Public License v2 or later (LGPLv2+)
 charset-normalizer             3.3.2       MIT License
 cssselect2                     0.7.0       BSD License
 dbus-python                    1.2.18      MIT License
 docutils                       0.19        BSD License; GNU General Public License (GPL); Public Domain; Python Software Foundation License
 ffmpeg-python                  0.2.0       Apache Software License
 freetype-py                    2.4.0       BSD License
 future                         0.18.3      MIT License
 idna                           3.6         BSD License
 imagesize                      1.4.1       MIT License
 lxml                           5.1.0       BSD License
 numpy                          1.26.3      BSD License
 opencv-python                  4.8.0.74    Apache Software License
 packaging                      23.2        Apache Software License; BSD License
 pycairo                        1.25.1      GNU Lesser General Public License v2 (LGPLv2); Mozilla Public License 1.1 (MPL 1.1)
 reportlab                      4.0.9       BSD License
 requests                       2.31.0      Apache Software License
 rlPyCairo                      0.3.0       BSD License
 snowballstemmer                2.2.0       BSD License
 sphinxcontrib-applehelp        1.0.8       BSD License
 sphinxcontrib-devhelp          1.0.6       BSD License
 sphinxcontrib-htmlhelp         2.0.5       BSD License
 sphinxcontrib-jsmath           1.0.1       BSD License
 sphinxcontrib-qthelp           1.0.7       BSD License
 sphinxcontrib-serializinghtml  1.1.10      BSD License
 svglib                         1.5.1       GNU Lesser General Public License v3 (LGPLv3)
 tinycss2                       1.2.1       BSD License
 urllib3                        2.1.0       MIT License
 webencodings                   0.5.1       BSD License
```

