# Simple Pipeline

## Code

**count.py** - contains two simple functions:
- `add(a, b)` - adds two numbers
- `subtract(a, b)` - subtracts second number

**test_count.py** - for testing:
- `test_add_positive` - testing in adding positive numbers
- `test_add_negative` - testing in adding negative numbers  
- `test_subtract` - testing in basic subtraction
- `test_subtract_negative` - testing in subtracting negative numbers

## CI/CD Pipeline

The `simple_pipeline.yml` runs automatically on every push and pull request:

1. **Checkout** - checks the code from the repo
2. **Set up Python** - installs Python 3.x on Ubuntu
3. **Install dependencies** - installs pytest
4. **Run tests** - run tests with `pytest -v`

If all tests pass, the pipeline is successful
