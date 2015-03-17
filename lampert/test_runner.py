from __future__ import absolute_import
from __future__ import division
import simplejson
from clint.textui import colored, puts

from lampert.suite import Suite


class TestRunner:
    def __init__(self, suitefile):
        with open(suitefile, 'r') as f:
            content = simplejson.loads(f.read())

        self.suite = Suite(
            content['suite'],
            content['slug'],
            content['tests'],
        )

    def run(self):
        results = self.suite.run()

        for result in results:
            puts(colored.magenta(result.name))
            puts(colored.green("Iterations: {}".format(result.result_count)))
            puts(colored.green("Average: {} ms".format(result.result_avg / 1000)))
            puts(colored.green("Max: {} ms".format(result.result_max / 1000)))
            puts(colored.green("Min: {} ms".format(result.result_min / 1000)))
            puts('\n')
