# -*- coding: utf-8 -*-

from learn_dvc import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_dvc.tests import run_cov_test

    run_cov_test(__file__, "learn_dvc.api", preview=False)
