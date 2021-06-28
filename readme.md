# Svyatoslav Kubakh home page

[![Site Build][ci-badge]][ci]
[![license][license-badge]][license]

## About

Based on [Pneumatic][pelican-pneumatic] theme 


## Setup

- Install  [Python][python] & [Python installer][python-pip]
- Install python dependencies: `pip install -r requirements.txt`
- Prepare images: `env bash ./prepare_icons.sh`

## Deployment routines

- Just generate site: `python -m pelican`
- Run internal server with live reload: `python -m pelican -lr`


## License

Licensed under the [MIT][license-spec] License. See the [license.md][license] file for more details.


[license]: ./license.md
[license-badge]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-spec]: https://opensource.org/licenses/MIT
[ci]: https://github.com/svyatoslav-kubakh/homepage/actions
[ci-badge]: https://github.com/svyatoslav-kubakh/homepage/workflows/CI/badge.svg
[python]: https://www.python.org/downloads/
[python-pip]: https://pypi.python.org/pypi/pip
[pelican-pneumatic]: https://github.com/svyatoslav-kubakh/pelican-pneumatic-theme
