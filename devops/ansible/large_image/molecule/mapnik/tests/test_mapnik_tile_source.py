"""Test mapnik based tile source."""

import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pip_packages(host):
    """Check python dependencies for mapnik tile source."""
    virtualenv = '~/.virtualenvs/large_image/bin/pip'
    packages = host.pip_package.get_packages(pip_path=virtualenv).keys()
    assert 'GDAL' in packages
    assert 'mapnik' in packages


def test_large_image_tiff_source(host):
    """Run large image mapnik tests."""
    activate = "source /root/.virtualenvs/large_image/bin/activate"
    run = "pytest /test_mapnik_tile_source.py"
    cmd = host.run("bash -c '{} && {}'".format(activate, run))
    assert cmd.stderr == ''