# Convert File Format

This program convers the file format.

## Support

- svg -> png

## Prepare

```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec --user $UID convert_file_format bash
$ cd /work
```

## Usage

```
usage: convert_file_format.py [-h] --convert_type {svg2png} --input_file INPUT_FILE --output_file
                              OUTPUT_FILE

Convert file format

options:
  -h, --help            show this help message and exit
  --convert_type {svg2png}
                        convert type
  --input_file INPUT_FILE
                        input file path
  --output_file OUTPUT_FILE
                        output file path
```

### SVG2PNG

```
$ python3 convert_file_format.py --convert_type svg --input_file <input_file> --output_file <output_file>
```

## Modules and Licenses

```
Name                           Version   License                                                                                          
Babel                          2.12.1    BSD License                                                                                      
Jinja2                         3.1.2     BSD License                                                                                      
MarkupSafe                     2.1.3     BSD License                                                                                      
Pillow                         10.0.0    Historical Permission Notice and Disclaimer (HPND)                                               
Pygments                       2.15.1    BSD License                                                                                      
Sphinx                         7.0.0     BSD License                                                                                      
alabaster                      0.7.13    BSD License                                                                                      
certifi                        2023.5.7  Mozilla Public License 2.0 (MPL 2.0)                                                             
charset-normalizer             3.1.0     MIT License                                                                                      
cssselect2                     0.7.0     BSD License                                                                                      
docutils                       0.19      BSD License; GNU General Public License (GPL); Public Domain; Python Software Foundation License 
freetype-py                    2.4.0     BSD License                                                                                      
idna                           3.4       BSD License                                                                                      
imagesize                      1.4.1     MIT License                                                                                      
lxml                           4.9.2     BSD License                                                                                      
packaging                      23.1      Apache Software License; BSD License                                                             
pycairo                        1.24.0    GNU Lesser General Public License v2 (LGPLv2); Mozilla Public License 1.1 (MPL 1.1)              
reportlab                      4.0.4     BSD License                                                                                      
requests                       2.31.0    Apache Software License                                                                          
rlPyCairo                      0.3.0     BSD License                                                                                      
snowballstemmer                2.2.0     BSD License                                                                                      
sphinxcontrib-applehelp        1.0.4     BSD License                                                                                      
sphinxcontrib-devhelp          1.0.2     BSD License                                                                                      
sphinxcontrib-htmlhelp         2.0.1     BSD License                                                                                      
sphinxcontrib-jsmath           1.0.1     BSD License                                                                                      
sphinxcontrib-qthelp           1.0.3     BSD License                                                                                      
sphinxcontrib-serializinghtml  1.1.5     BSD License                                                                                      
svglib                         1.5.1     GNU Lesser General Public License v3 (LGPLv3)                                                    
tinycss2                       1.2.1     BSD License                                                                                      
urllib3                        2.0.3     MIT License                                                                                      
webencodings                   0.5.1     BSD License                                                                                      
```

