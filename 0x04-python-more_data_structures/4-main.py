#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = {"python", "c", "javascript"}
set_2 = {"bash", "c", "ruby", "per;"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
