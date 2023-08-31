"""

Task 4: Optional

After successfully completing your implementation of the example code on your own datafile, 
then you may copy your working code into another file (process_streaming_yourname99.py) 
and send the output to out99.txt (which should match out9.txt above). 

"""

# Import from Python Standard Library

import csv
import socket
import time
import logging



# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Declare program constants (typically constants are named with ALL_CAPS)

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "netflix_titles.csv"
OUTPUT_FILE_NAME = "out99.txt"




# Define program functions (bits of reusable code)

def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
   
    show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = row
    
    # use an fstring to create a message from our data
    fstring_message = f"[{type}, Title: {title}, Release: {release_year}, Will be Added: {date_added}]"
    
    
   # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared message: {fstring_message}")
    return MESSAGE


def stream_row(input_file_name, address_tuple):
    """Read from input file and stream data."""
    logging.info(f"Starting to stream data from {input_file_name} to {address_tuple}.")

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")


        # use socket enumerated types to configure our socket object
        # Set our address family to (IPV4) for 'internet'
        # Set our socket type to UDP (datagram)
        ADDRESS_FAMILY = socket.AF_INET 
        SOCKET_TYPE = socket.SOCK_DGRAM 

        # Call the socket constructor, socket.socket()
        # A constructor is a special method with the same name as the class
        # Use the constructor to make a socket object
        # and assign it to a variable named `sock_object`
        sock_object = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
        
        rows = list(reader)
        
        last_processed_index = 0  # Track the index 

        with open(OUTPUT_FILE_NAME, "w") as output_file:
              logging.info(f"Opened for writing: {OUTPUT_FILE_NAME}.")
              while True: 
                  for i in range(last_processed_index, len(rows)):
                     row = rows[i]
                     MESSAGE = prepare_message_from_row(row)
                     sock_object.sendto(MESSAGE, address_tuple)
                     output_file.write(str(MESSAGE) + "\n")
                     logging.info(f"Sent and wrote: {MESSAGE} on port {PORT}.")

                     last_processed_index = len(rows)  # Update the index 
                     
                     time.sleep(3)

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, ADDRESS_TUPLE)
        logging.info("Streaming complete!")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
