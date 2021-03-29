SHELL:=/usr/bin/env bash

update: docs/supplementals/typecasts/defaults.yaml


docs/supplementals/typecasts/defaults.yaml: serialize_casts_to_yaml.py pyproject.toml
	python serialize_casts_to_yaml.py > docs/supplementals/typecasts/defaults.yaml


.PHONY: generate
generate:
	mkdir -p docs/_generated/custom-types
	curl https://raw.githubusercontent.com/python-platonic/platonic-sqs/master/tests/test_queue/test_send_and_receive/test_inheritance.py | head -n 26 > docs/_generated/custom-types/test_inheritance.py
