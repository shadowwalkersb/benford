# Benford's Law

## Installation
```shell
git clone https://github.com/shadowwalkersb/benfords_law.git
cd benfords_law
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```shell
python app.py
```

1. In your browser, navigate to http://127.0.0.1:5000 or one of the addresses displayed after running the previous command.
2. Click `Browse` and select `census_2009.txt` or another data file.
2. Click `Upload`.
3. Select a column number to process, `-1` for `census_2009.txt`. Negative numbers represent columns from end.
4. Click `Run`.


## Docker
```shell
docker run -it -p 5000:5000 shadowwalker/benford
```

1. In your browser, navigate to http://127.0.0.1:5000 or one of the addresses displayed after running the previous command.
2. Click `Browse` and select a data file.
2. Click `Upload`.
3. Select a column number to process. Negative numbers represent columns from end.
4. Click `Run`.


## Tests
To run the tests, run the following in the top directory of the repository.
```shell
pytest . -vv -s
```
