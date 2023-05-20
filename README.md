# Lambda Project Template

```shell
# Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Tests
python3 -m pip install -r requirements-tests.txt
python3 -m pytest --verbose --cov=tests
pytest --cov=src --cov-report term-missing --cov-report=html
```

# Referencies
* [Manage Python ENVs](https://ljvmiranda921.github.io/notebook/2021/05/12/how-to-manage-python-envs/)
* [Python Makefile](https://venthur.de/2021-03-31-python-makefiles.html)
* [Python with virtualenv](https://www.dinotools.de/en/2019/12/23/use-python-with-virtualenv-in-makefiles/)
* [Python Makefile](https://earthly.dev/blog/python-makefile/)