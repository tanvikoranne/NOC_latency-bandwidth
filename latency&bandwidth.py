import re
def get_timestamp(line):
    """Extracts the timestamp from a simulator output line.

    Args:
        line (str): A line from the simulator output.

    Returns:
        int: The timestamp value (cycles) or None if not found.
    """
    match = re.search(r"cycle:(\d+)", line)
    if match:
        return int(match.group(1))
    else:
        return None
def get_transaction_type(line):
    """Identifies the transaction type (read or write) from a simulator output line.
    Args:
        line (str): A line from the simulator output.

    Returns:
        str: The transaction type ("Rd" for read, "Wr" for write) or None if not identified.
    """
    if "Rd" in line:
        return "Rd"
    elif "Wr" in line:
        return "Wr"
    else:
        return None
def average_latency(timestamps):
    """Calculates the average latency from a list of timestamps.
    Args:
        timestamps (list): A list of timestamps (cycles).

    Returns:
        float: The average latency (cycles) or None if the list is empty.
    """
    if not timestamps:
        return None  # Handle empty list
    total_latency = sum(timestamps)
    average_latency = total_latency / len(timestamps)
    return average_latency
def bandwidth(timestamps, data_width):
    """Calculates the bandwidth based on timestamps and data width.

    Args:
        timestamps (list): A list of timestamps (cycles).
        data_width (int): The data width in bytes per transfer.

    Returns:
        float: The bandwidth in Mbps, or None if the list is empty.
    """
    if not timestamps:
        return None  # Handle empty list
    total_cycles = timestamps[-1] - timestamps[0]  # Assuming timestamps are in order
    total_bytes = len(timestamps) * data_width
    bandwidth_mbps = total_bytes / (total_cycles * 10**6)  # Convert to Mbps
    return bandwidth_mbps
def process_simulator_output(trace):
    """Processes the simulator output list of lists to calculate average latency and bandwidth.

    Args:
        trace (list): A list of lists, where each inner list represents a line from the simulator output.

    Prints:
        The average read latency, average write latency, average latency, and bandwidth.
        Also prints an error message if the trace data is empty.
    """

    # Initialize variables
    rd_latencies = []
    wr_latencies = []
    for line in trace:
        # Extract timestamp and transaction type from each line
        timestamp = get_timestamp(line[0])  # Assuming timestamps are in the first element of each inner list
        transaction_type = get_transaction_type(line[1])  # Assuming transaction types are in the second element

        if timestamp is not None and transaction_type is not None:
            # Add valid timestamps to respective lists based on transaction type
            if transaction_type == "Rd":
                rd_latencies.append(timestamp)
            else:
                wr_latencies.append(timestamp)

    # Calculate average latency and bandwidth (if data is valid)
    if rd_latencies or wr_latencies:
        avg_rd_latency = average_latency(rd_latencies)
        avg_wr_latency = average_latency(wr_latencies)
        if avg_rd_latency is not None and avg_wr_latency is not None:
             avg_latency = (avg_rd_latency + avg_wr_latency) / 2
        else:
            print("Unable to calculate average latency due to missing data.")
        data_width = 32  # Assuming data width is 32 bytes (replace with actual value)
        bandwidth_mbps = bandwidth(rd_latencies + wr_latencies, data_width)  # Combine timestamps for bandwidth

        # Print results
        print("Average Read Latency:", avg_rd_latency, "cycles")
        print("Average Write Latency:", avg_wr_latency, "cycles")
        print("Average Latency:", avg_latency, "cycles")
        print("Bandwidth:", bandwidth_mbps, "Mbps")
    else:
        print("Empty trace data. Unable to calculate metrics.")
# Replace with our actual simulator output (list of lists)
process_simulator_output(simulator_trace)