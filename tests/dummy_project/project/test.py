from twisted.internet import defer
from twisted.internet import reactor
from twisted.trial import unittest


def sleep(seconds):
    d = defer.Deferred()
    reactor.callLater(seconds, d.callback, seconds)
    return d


class Test(unittest.TestCase):
    @defer.inlineCallbacks
    def setUp(self):
        self.waited = False
        yield sleep(0)
        self.waited = True

    def test_main(self):
        self.assertTrue(self.waited)
