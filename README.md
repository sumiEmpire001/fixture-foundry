# Fixture Foundry

Generate reproducible **synthetic** people and scores for application development and tests. No external dependencies or real personal information.

## Usage

```bash
python app.py --count 20 --seed 42 --format json
python app.py --count 100 --seed 42 --format csv --output sample.csv
python -m unittest discover -s tests -v
```

Fields: `id`, `name`, `score` (0–100), `active`. The same seed and count produce identical results. Exit code 0 indicates success; 2 indicates invalid input or file error.

## Limitations

Data is fictional and not suitable for statistical inference, security tests requiring cryptographic randomness, or production identity generation.
