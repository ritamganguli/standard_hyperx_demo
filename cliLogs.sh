#!/bin/bash

# Input and output file paths
LOG_FILE="hyperexecute-cli.log"
TEMP_FILE="temp.json"
OUTPUT_FILE="hyperexecute-cli.json"

# Convert JSONL to a JSON array
{
  echo "["
  sed 's/,$//' "$LOG_FILE" | sed '$!s/$/,/'  # Add commas between lines except the last
  echo "]"
} > "$TEMP_FILE"

# Format the JSON properly
if command -v jq &>/dev/null; then
  # Use jq if installed
  jq '.' "$TEMP_FILE" > "$OUTPUT_FILE"
elif command -v python3 &>/dev/null; then
  # Use Python for formatting if jq isn't available
  python3 -c "import json, sys; print(json.dumps(json.load(sys.stdin), indent=4))" < "$TEMP_FILE" > "$OUTPUT_FILE"
else
  echo "Error: Neither jq nor Python is installed to format the JSON."
  exit 1
fi

# Clean up temporary file
rm "$TEMP_FILE"

echo "Conversion and formatting complete. Output saved to $OUTPUT_FILE"
