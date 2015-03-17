from __future__ import absolute_import
import argparse

from lampert.test_runner import TestRunner

def main():
    from lampert.cli import parser
    args = parser.parse_args()

    runner = TestRunner(args.suitefile)
    runner.run()
