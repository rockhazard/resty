# Resty: Query Domain Status Codes

### Come Again?

This generates a report of [HTTP REST status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for given domains.

### Why?

So folks can figure out if their domains are working properly.

### Features
- Reports HTTP REST status codes for an arbitrary number of given urls.
- Tests the SSL certificates for given urls, reporting any errors.

### Dependencies
If not using the binaries, Python 3.6+ and the requests library are required.

### Usage

type `resty.py -h` at a terminal.

### ToDo

- Prune bookmark files of dead links
- Accept json and csv files as input
- Output report in json, csv, and plain text file, instead of just to stdout.