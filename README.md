# NOC_latency-bandwidth
This code provides functions to process simulator output and calculate key metrics for Network-on-Chip (NOC) analysis, including average read latency, average write latency, average latency, and bandwidth.

Features:

Extracts timestamps and transaction types (read/write) from simulator output lines.
Calculates average latency for both read and write transactions.
Calculates overall average latency considering both read and write transactions (weighted average).
Calculates bandwidth based on total transferred bytes and elapsed time.
Requirements:

Operating System: Compatible with most major operating systems (Windows, macOS, Linux)
Python: Version 3.x (check with python --version or python3 --version in your terminal)
re module: Included in the Python standard library (no additional installation needed)
Setting Up the Environment:

Verify Python Version: Ensure you have Python 3.x installed. If not, download and install it from the official Python website (https://www.python.org/downloads/).
Verify re Module: The code utilizes the re module, which is included by default in Python. No additional setup is required.
Running the Code:

Save the Script: Save the provided code as a Python file (e.g., noc_analysis.py).

Open Terminal/Command Prompt: Open a terminal or command prompt window and navigate to the directory where you saved the script.

Run the Script: Execute the script using the following command:

Bash
python noc_analysis.py
Use code with caution.
(Replace python with python3 if your system requires specifying the Python 3 version)

Output:

The script will process your simulator output data (replace the placeholder simulator_trace variable) and print the following metrics:

Average Read Latency (cycles)
Average Write Latency (cycles)
Average Latency (cycles) - weighted average of read and write latencies
Bandwidth (Mbps)
If the provided trace data is empty, the script will print an error message.

Code Breakdown:

get_timestamp(line): Extracts the timestamp (cycles) from a simulator output line using regular expressions.
get_transaction_type(line): Identifies the transaction type (read or write) from a simulator output line.
average_latency(timestamps): Calculates the average latency from a list of timestamps.
bandwidth(timestamps, data_width): Calculates the bandwidth based on timestamps and data width (bytes per transfer).
process_simulator_output(trace): Processes the simulator output, calculates metrics, and prints the results.
Notes:

The code assumes timestamps are in the first element of each inner list and transaction types are in the second element. Adjust these assumptions based on your actual simulator output format.
The code assumes a fixed data width for transfers. Modify the data_width assignment if your data size varies.
Further Considerations:

Error handling can be extended to handle cases with invalid data formats in the simulator output.
The code could be made more flexible by allowing configuration of data width and potentially other parameters.
Additional Information:

This script provides a basic framework for NOC analysis. You can extend it to incorporate more complex calculations or visualizations based on your specific needs.
