doc:
	pandoc README.md -o README.md --filter include_filter.py

test:
	pandoc README.md -o README.1.md --filter include_filter.py
	pandoc README.1.md -o README.2.md --filter include_filter.py
	diff README.1.md README.2.md

venv:
	python3 -m venv venv
	. venv/bin/activate

.PHONY: doc test deps clean

deps: venv
	. venv/bin/activate
	pip3 install -r requirements.txt

clean:
	rm -rf venv
	rm -f README.1.md README.2.md
