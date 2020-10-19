
PY = python3

# if python3 doesn't exist, set it to python
ifneq ($(shell which python3 1>&2 2> /dev/null; echo $$?),0)
	PY = python
endif

run:
	$(PY) cyb_python/vigenere.py ${ARGS}