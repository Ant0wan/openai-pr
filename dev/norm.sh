#!/bin/sh
find src/ -type d -exec pylint {} \;
find src/ -type d -exec pycodestyle --show-source --show-pep8 {} \;
