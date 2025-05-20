# Python-project Difference Generator
[![Build](https://github.com/Olga877/python-project-50/actions/workflows/build.yml/badge.svg)](https://github.com/Olga877/python-project-50/actions/workflows/build.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Olga877_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Olga877_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Olga877_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Olga877_python-project-50)

### Description

*Difference Generator* is a program that determines the difference between two data structures. This is a popular task, for which there are many online services, for example, jsondiff. A similar mechanism is used, for example, when outputting tests or when automatically tracking changes in configuration files.  

### Utility Capabilities:
- Different input formats support: yaml, json
- Report generating in plain text, stylish and json formats

### Usage example:
```
gendiff --format plain filepath1.json filepath2.json

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```

gendiff .json
[![asciicast](https://asciinema.org/a/t61I6hZiC3rAt89srtOWKMFGq.svg)](https://asciinema.org/a/t61I6hZiC3rAt89srtOWKMFGq)
gendiff .yml
[![asciicast](https://asciinema.org/a/DZri9HeVhAfQBboro91wRRbOj.svg)](https://asciinema.org/a/DZri9HeVhAfQBboro91wRRbOj)
gendiff stylish formatter
[![asciicast](https://asciinema.org/a/kvwIQAClaH6DR3EufxQeO59J3.svg)](https://asciinema.org/a/kvwIQAClaH6DR3EufxQeO59J3)
gendiff plain formatter
[![asciicast](https://asciinema.org/a/GunzYEOFEmh0uq7rVVWPoja4m.svg)](https://asciinema.org/a/GunzYEOFEmh0uq7rVVWPoja4m)
gendiff json formatter
[![asciicast](https://asciinema.org/a/o7DBEqyp3H5llYqWTANNJrcD6.svg)](https://asciinema.org/a/o7DBEqyp3H5llYqWTANNJrcD6)
