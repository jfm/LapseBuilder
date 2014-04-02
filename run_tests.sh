#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/home/jfm/Development/LapseBuilder/lapsebuilder

python test/test_system_tools.py
python test/test_image_tools.py
