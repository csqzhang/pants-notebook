# pants-notebook

## Setup (OSX tested):
```bash
conda env create -f env.yaml
```
Download pants binary
```
curl https://github.com/pantsbuild/pants/releases/download/release_2.14.0/pants.2.14.0.pex --output pants
chmod +x pants
```
## Tests
Test passed by running
```bash
pytest tests/test_notebooks.py
```
however, it fails in Pants
```bash
./pants test tests/test_notebooks.py
```