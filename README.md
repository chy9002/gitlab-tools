# Gitlab Tool

This is an simple tool for gitlab api.

# Dependencies

python 3.x

## Install dependencies

```shell
pip install -r requirements.txt
```

## How to use

```shell
python  app.py [--reset|--setup|-i|-m]
--reset      reset group and project
--setup      setup api url and token
-i           Download issues(default)
-m           Download merge requests
```