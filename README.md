# cli-spinner

Spinners and progress bars that degrade gracefully when not a TTY.

## Why

Written while learning the language properly, and kept because it still works.

## Install

```bash
pip install cli-spinner
```

## Usage

```python
from cli_spinner import cliSpinner

result = cliSpinner("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
