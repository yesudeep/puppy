#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import logging
import sys
import tokenize
import token
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from pprint import pprint

class ParseError(Exception):
    _message = None

    def set_message(self, m):
        self._message = m
    message = property(lambda: self._message, set_message)

    def __init__(self, expression, message='Parse error'):
        self.expression = expression
        self.message = message

    def __repr__(self):
        return 'ParseError in expression ' + self.expression + ' -- ' + self.message

class IncompleteQueryError(ParseError):
    pass

class InvalidQueryError(ParseError):
    pass

class InvalidKeyError(InvalidQueryError):
    pass

class InvalidIndexError(InvalidQueryError):
    pass

class InvalidTokenError(ParseError):
    pass

class QueryDict(dict):
    def query(self, query, default_value=None):
        query_string = StringIO(query).readline
        tokens = tokenize.generate_tokens(query_string)

        val = self

        def get_negative_at(value, index_string, default=None):
            index = int(index_string, 10)
            return value[-index]

        def get_at(value, index_string, default=None):
            index = int(index_string, 10)
            return value[index]

        func = QueryDict.get
        tokens = [tok for tok in tokens]
        for i, (token_type, token_string, (begin_row, begin_column), (end_row, end_column), line_number) in enumerate(tokens):
            if token_type == token.ENDMARKER:
                break
            elif token_type == token.NAME or token_type == token.NUMBER:
                try:
                    val = func(val, token_string)
                    if isinstance(val, dict):
                        val = QueryDict(val)
                except TypeError:
                    return default_value
                except IndexError:
                    return default_value
                #logging.debug('Parsing string, obtained %s' % val)
            elif token_type == token.OP:
                try:
                    next_token_type, next_token_string, a, b, c = tokens[i + 1]
                except IndexError:
                    raise IncompleteQueryError(query_string, "incomplete query string syntax")
                if token_string == '.':
                    if next_token_type == token.NAME:
                        func = QueryDict.get
                    else:
                        raise InvalidKeyError(query_string, "expected key, got `%s' instead" % token_string)
                elif token_string == '-':
                    if next_token_type == token.NUMBER:
                        func = get_negative_at
                    else:
                        raise InvalidIndexError(query_string, "expected index, got `%s' instead" % token_string)
                elif token_string == '[':
                    if next_token_type == token.NUMBER:
                        func = get_at
                    elif next_token_type == token.OP and next_token_string == '-':
                        pass
                    else:
                        raise InvalidIndexError(query_string, "expected index, got `%s' instead" % token_string)
                elif token_string == ']':
                    #func = QueryDict.get
                    pass
            else:
                raise InvalidTokenError(query_string, "`%s' is an invalid token" % token_string)

        return val

if __name__ == '__main__':
    lee = xrange(0, 40)

    d = QueryDict({
        'foo': {
            'bar': [
                {'cee': 0},
                {'cee': 1},
                {'cee': 2},
            ],
            'bam': {
                'boo': [0, 1, 2, 3],
                'lee': lee
            }
        }
    })

    tests = [
        ('foo.bar[1].cee', 1),
        ('.foo.bar[1].cee', 1),
        ('foo.bar[0].cee', 0),
        ('foo.bar[-1].cee', 2),
        ('foo.bar[-2].cee', 1),
        ('foo.bar[-3].cee', 0),
        ('foo.bam.boo', [0, 1, 2, 3]),
        ('foo.bam.lee', lee),
    ]

    # Dictionary values returned are instances of QueryDict so you can chain them.
    assert d.query('foo.bam').query('boo') == [0, 1, 2, 3]
    print 'PASS'

    for query, result in tests:
        assert d.query(query) == result
        print 'PASS'


