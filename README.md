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
            "test": "read", // (view|read|all_docs)
            "database": "http://localhost:5984/commcarehq" // database to run tests against
            "params": {}, // Optional params to be appended to couchdb url
            "repeat": 100, // Number of times this test is run
            ... // Other args depending on the test
        }
    ]
}

```

### read test

```
{
    "test": "read",
    "database": "http://localhost:5984/commcarehq"
    "params": {},
    "repeat": 100,
    "ids": [] // ids of docs to read
}
```
### all_docs test
```
{
    "test": "all_docs",
    "database": "http://localhost:5984/commcarehq"
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
    "test": "view",
    "database": "http://localhost:5984/commcarehq"
    "params": {},
    "repeat": 100,
    "view": "_design/app_manager/_view/applications" // view to test the database on
}
```

You can view an example in `tests/data/test_suite.json`
