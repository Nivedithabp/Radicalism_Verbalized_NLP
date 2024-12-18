#!/bin/bash
# To run the topic modeling script
# NOTE: change input directory/input file to change the input data to be processed
python3 ./src/__main__.py topic --input=./sample_data/37-septembre-2008.pdf/ --output=./src/topic_modeling/topic_results/ --name="test1" --uri="" --auth_username="" --auth_password=""
