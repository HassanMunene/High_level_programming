## Metric computation of log file entry
The purpose of this exercise is to read log file entries in a specific format from the standard input(stdin), compute various metrics for each entry, and then calculate aggregated ststistics on those metrics.

The input at first consist of log file entries with fields for IP address, date, HTTP request type, status code and file size.

After 10 lines of these entries or after being interrupted with a keyboard(CTRL + C) the script calculates and prints the following statistics since the beginning:

1. Total file size: The sum of all file size from prevoius entries.
1. Number of lines by status code: The number of lines with each possible status code that appears in the previous entries. 

overall the purpose of this code is to provide insights into the usage of a web server by analyzing the log file entries and presenting useful statistics

