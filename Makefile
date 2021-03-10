SHELL:=/usr/bin/env bash

update: docs/supplementals/typecasts/defaults.yaml


docs/supplementals/typecasts/defaults.yaml: serialize_casts_to_yaml.py pyproject.toml
	python serialize_casts_to_yaml.py > docs/supplementals/typecasts/defaults.yaml
