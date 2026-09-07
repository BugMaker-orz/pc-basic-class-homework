.PHONY: all clean

all: stats.txt report.txt

stats.txt: data.csv stats.py
	python3 stats.py

report.txt: stats.txt report.py
	python3 report.py

clean:
	rm -f stats.txt report.txt
