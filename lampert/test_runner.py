from __future__ import absolute_import
import simplejson
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
        self.suite.run()
