#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
from sacred.observers.mongo import MongoDbOption


def test_parse_mongo_db_arg():
    assert MongoDbOption.parse_mongo_db_arg('foo') == ('localhost:27017',
                                                       'foo', '')


def test_parse_mongo_db_arg_collection():
    assert MongoDbOption.parse_mongo_db_arg('foo.bar') == ('localhost:27017',
                                                           'foo', 'bar')


def test_parse_mongo_db_arg_hostname():
    assert MongoDbOption.parse_mongo_db_arg('localhost:28017') == \
        ('localhost:28017', 'sacred', '')

    assert MongoDbOption.parse_mongo_db_arg('www.mymongo.db:28017') == \
        ('www.mymongo.db:28017', 'sacred', '')

    assert MongoDbOption.parse_mongo_db_arg('123.45.67.89:27017') == \
        ('123.45.67.89:27017', 'sacred', '')


def test_parse_mongo_db_arg_hostname_dbname():
    assert MongoDbOption.parse_mongo_db_arg('localhost:28017:foo') == \
        ('localhost:28017', 'foo', '')

    assert MongoDbOption.parse_mongo_db_arg('www.mymongo.db:28017:bar') == \
        ('www.mymongo.db:28017', 'bar', '')

    assert MongoDbOption.parse_mongo_db_arg('123.45.67.89:27017:baz') == \
        ('123.45.67.89:27017', 'baz', '')


def test_parse_mongo_db_arg_hostname_dbname_collection_name():
    assert MongoDbOption.parse_mongo_db_arg('localhost:28017:foo.bar') == \
        ('localhost:28017', 'foo', 'bar')

    assert MongoDbOption.parse_mongo_db_arg('www.mymongo.db:28017:bar.baz') ==\
        ('www.mymongo.db:28017', 'bar', 'baz')

    assert MongoDbOption.parse_mongo_db_arg('123.45.67.89:27017:baz.foo') == \
        ('123.45.67.89:27017', 'baz', 'foo')
