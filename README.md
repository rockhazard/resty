# Resty: Query REST Status Codes

### Come Again?

This generates a report of [HTTP REST status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for the given domains.

### Why?

So folks can figure out if their domains are working properly.

### Features
- Retrieves HTTP REST status codes for an arbitrary number of given urls.
- Outputs report to terminal, csv file, or both.
- Tests SSL certificates for given urls and reports errors.

### Dependencies
If not using the binaries, Python 3.6+ and the requests library are required.

### Usage

Type `resty.py -h` at a terminal.

### ToDo

- Prune bookmark files of dead links
- Accept json and csv files as input
- Output report in json.