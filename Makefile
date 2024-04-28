.PHONY: all

all: db_connections.py clean.py Data_transformation.py split.py model_training.py model_evaluation.py evaluation_results.py

db_connections.py:
	python src/components/db_connections.py xdr_data

clean.py:
	python src/components/clean.py xdr_data_table

Data_transformation.py:
	python src/components/Data_transformation.py

split.py:
	python src/components/split.py

model_training.py:
	python src/components/model_training.py

model_evaluation.py:
	python src/components/model_evaluation.py

evaluation_results.py:
	python src/components/evaluation_results.py





