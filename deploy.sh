rm -r
rm -r build
rm -r dist
pandoc --from=markdown --to=rst README.md --output=readme.rst
python setup.py bdist_wheel --universal
python setup.py sdist
twine upload dist/*
open https://pypi.python.org/pypi/draw-compose