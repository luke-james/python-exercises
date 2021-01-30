#!/bin/bash
excercise_name="$1"
if [ $excercise_name != "" ]; then
  touch $(pwd)/src/"$1".py
  touch $(pwd)/tests/test_"$1".py
fi
