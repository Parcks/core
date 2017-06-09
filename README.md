# Parcks
See [the official website](http://parcks.setarit.com/) for more info.
Parcks is a project from [Setarit](http://setarit.com)

## Running the tests
To run the test fire up your terminal and run `python -m unittest discover` or `python3 -m unittest discover` for Python 3.3+

## To do
* Fix double download if unverified plugin
* Support all linux distro families
* Update package list (Debian: `apt-get update`) before installing once a week
* Continue the execution of the remaining plugins if one is unverified (currently this kills Parcks)
* Improve test coverage (currently (v.2.1.0) 89%)
* Make Parcks a standalone package manager

## Tested distros
* Ubuntu
* Debian
* Fedora

All derivates of the above linux families should work. If it is not the case, please open an issue.

## Contributing
See the [Contribution file](https://github.com/Parcks/core/blob/master/CONTRIBUTING.md).

### Setting up the development environment
1. Clone the repository
2. If not already installed, install `pip`
3. Run `pip install -Ur requirements` to install the Python requirements

## Maintainer
* [JValck](https://github.com/JValck) - [Twitter](https://twitter.com/realJValck)
