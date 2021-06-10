run_download_data:
	python3 download_ECCC_data_hourly.py

install_requirements:
	pip install -r requirements.txt && sudo apt-get update

formatting:
	safety check
	isort .
	black .
	flake8 .

install_requirements_dev:
	pip install -r requirements_dev.txt

docker_build:
	docker build . -t download_ECCC_data_hourly

docker_run:
	docker run download_ECCC_data_hourly

