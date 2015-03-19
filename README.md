# Loveseat
Loveseat, a simple couchdb benchmarking tool, provides you with one-on-one time for you and couchdb.

## Installation

```
pip install loveseat
```

## Usage

```
loveseat mysuitefile.json
```

## Suitefiles

Suitefiles tell what tests loveseat should run. There are currently three different types of tests: read, all_docs, and view.

Below is a generic template for a suite:

```
{
    "suite": "Example Suite",
    "slug": "example_suite",
    "tests": [
        {
            "name": "My test name",
            "test": "read", // (view|read|all_docs)
            "databases": ["http://localhost:5984/commcarehq"] // databases to run tests against
            "params": {}, // Optional params to be appended to couchdb url
            "headers": {}, // Any headers you wish to send along with the request
            "repeat": 100, // Number of times this test is run
            ... // Other args depending on the test
        }
    ]
}

```

### read test

```
{
    "name": "My test name",
    "test": "read",
    "databases": ["http://localhost:5984/commcarehq"]
    "params": {},
    "repeat": 100,
    "ids": [] // ids of docs to read
}
```
### all_docs test
```
{
    "name": "My test name",
    "test": "all_docs",
    "databases": ["http://localhost:5984/commcarehq"]
    "params": { // may be prudent to apply params when testing all_docs depending on db size
        startkey: "",
        endkey: ""
    },
    "repeat": 100,
}
```
### view test
```
{
    "name": "My test name",
    "test": "view",
    "databases": ["http://localhost:5984/commcarehq"]
    "params": {},
    "repeat": 100,
    "view": "_design/app_manager/_view/applications" // view to test the database on
}
```

You can view an example in `tests/data/test_suite.json`

### Advanced database configuration

Sometimes couch requires some extra parameters to connect to a database. Loveseat allows you to set custom headers and paramters to any database you list. Example:

```
{
    "name": "My test name",
    "test": "view",
    "databases": [
        "http://localhost:5984/commcarehq",
        { "url": "http://another/db", "params": {...}, "headers": {...}, "slug": "human name" }
    ]
    "params": {},
    "headers": {}
    ...
}
```

Now loveseat knows to use those parameters when calling that database. Internally loveseat takes the string database parameters and turns them into an object, using the higher level `params` and `headers` keys as defaults. So, if you have this structure:

```
{
    "name": "My test name",
    "test": "view",
    "databases": [
        "http://localhost:5984/commcarehq",
        { "url": "http://another/db", "headers": { "my": "header" } }
    ]
    "params": { "my": "param" },
    "headers": { "other": "header" }
    ...
}
```

Then the resulting database configuration for `http://another/db` would be:

```
{
    "url": "http://another/db",
    "headers": { "my": "header" },
    "params": { "my": "param" }
}
```
This allows you to easily specify multiple databases without have to rewrite a bunch of configuration.

## Roadmap

- More metrics
- 'write' tests
- Better test coverage
- Sensible error handling
- Weird behavior when sending loads of requests at once
