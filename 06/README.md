﻿
# 06

##### Run coverage:
```
pip install pytest-cov
pytest --cov=lru_cache --cov-branch -vvv -x test_lru_cache.py
```
Coverage report is in `coverage_report.txt`

---
##### Run pylint:
```
pip install pylint
pylint --output-format=colorized -v lru_cache.py
```
Linter report is in `pylint_report.txt`
