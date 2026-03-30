# DROUGHTS

Repository for collaboration on workflows for the droughts hazard.

[<img src="https://raw.githubusercontent.com/CLIMAAX/crabook/main/crabook/logo.png" height="100" />](https://climaax.eu)

Part of the [Climate Risk Assessment Handbook](https://handbook.climaax.eu/notebooks/workflows/droughts.html).


## Workflows

- [Relative drought](01_relative_drought/)
- [Agricultural drought](02_agriculture_drought/)


## How to run

See our [how to use risk workflows](https://handbook.climaax.eu/notebooks/workflows_how_to.html) page in the Handbook for more information.

### Launch a binder session

Binder sessions are not persistent and may not provide the necessary computing resources to run all workflow steps.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/climaax/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252FCLIMAAX%252FDROUGHTS%26urlpath%3Dlab%252Ftree%252FDROUGHTS%252F%26branch%3Dmain)

### Local setup with conda

```bash
# Clone the workflow repository
git clone git@github.com:CLIMAAX/DROUGHTS.git
cd DROUGHTS

# Create a new environment and activate it
conda env create -f environment.yml

# Start the JupyterLab from within the created environment
conda activate climaax_droughts
jupyter lab
```

## How to contribute

See our [contributions](https://handbook.climaax.eu/community/contribute.html) page in the Handbook.

## License

`Apache-2.0 OR CC-BY-4.0` ([SPDX license identifier](https://spdx.dev/learn/handling-license-info/)).

## Acknowledgements

CLIMAAX has received funding from the European Union’s Horizon Europe – the Framework Programme for Research and Innovation (2021-2027) under grant agreement No. 101093864.
