# Riksbank
Read from riksbankens [REST API](https://developer.api.riksbank.se/) to pandas.
Riksbank is the Swedish central bank and this API allows to query exchange rates, as well as intrest rates.

## Requirements
You will need a API key for the API.

## Usage
Check the tests for some examples.
```python
from riksbank import riksbank
query = riksbank.Query(user, key)
res = query.get_observations('SEKEURPMI', '2024-01-01', '2024-02-01')
```
