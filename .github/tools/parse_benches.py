#!/bin/python3

# Converts the output of:
#   `$ substrate benchmark --pallet "*" --extrinsic "*" --steps 0`
# into a readable JSON format. The substrate output is read from a file provided as a CLI argument.
#
# Usage:
# $ parse_benches.py /path/to/file.txt
#
# Example file content (input):
# ```
# Pallet: "balances", Extrinsic: "transfer", Lowest values: [], Highest values: [], Steps: [0], Repeat: 1
# Pallet: "balances", Extrinsic: "transfer_best_case", Lowest values: [], Highest values: [], Steps: [0], Repeat: 1
# <...>
# ```
#
# Example JSON format (output):
# ```
# [
#     {
#         "pallet": "balances",
#         "extrinsic": "transfer"
#     },
#     {
#         "pallet": "balances",
#         "extrinsic": "transfer_best_case"
#     },
#     <...>
# ]
# ```

import sys
import json
import os

try:
    Input = sys.argv[1]

    if not Input:
        raise Exception("Provide an input file as argument")

    # Contains the output
    in_file = open(Input, 'r')

    full_list = []
    for line in in_file.readlines():
        if not line.startswith("Pallet: "):
            continue

        # Parse file and collect required values.
        # For each value, remove `"` at the beginning and `",` at the end
        parts = line.split(' ')
        pallet = parts[1][1:-2]
        extrinsic = parts[3][1:-2]

        full_list.append(
            {
                "pallet": pallet,
                "extrinsic": extrinsic
            }
        )

    # Print pretty JSON
    print(json.dumps(full_list, indent=4))

except IndexError:
    print("No input file provided")
    print("Usage:", os.path.basename(__file__), "/path/to/file.txt")
except OSError as e:
    print("Failed to read from provided input file:", e)
except:
    print("Something went wrong:", sys.exc_info()[0])
    in_file.close()
else:
    in_file.close()
