from pathlib import Path
from datetime import datetime
import re


class HeartbeatReader:
    def __init__(self, filename, log_filename):
        self.filename = Path(__file__).parent / filename
        self.log_filename = Path(__file__).parent / log_filename
        self.timestamp_pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")

    @staticmethod
    def parse_timestamp(timestamp):
        return datetime.strptime(timestamp, "%H:%M:%S")
    
    def process_log(self):
        with open(self.filename, mode="r") as f:
            lines = f.readlines()
        
        lines.reverse()
        previous_time = None
        

        with open(self.log_filename, mode="w") as log_file:
            for line in lines:
                match = self.timestamp_pattern.search(line)
                if match:
                    timestamp_str = match.group(1)
                    current_timestamp = self.parse_timestamp(timestamp_str)
                    #log_file.write(f"Parsed timestamp: {timestamp_str}\n")

                    if previous_time is not None:
                        result_seconds = (current_timestamp - previous_time).total_seconds()

                        if 30 < result_seconds < 32:
                            log_file.write(f"WARNING: Heartbeat interval is {result_seconds} seconds at {timestamp_str}\n")
                        elif result_seconds >= 32:
                            log_file.write(f"ERROR: Heartbeat interval is {result_seconds} seconds at {timestamp_str}\n")

                        #log_file.write(f"Interval: {result_seconds} seconds\n")

                    previous_time = current_timestamp
        
if __name__ == "__main__" :
    heartbeat_reader = HeartbeatReader('hblog', 'hb.log')
    heartbeat_reader.process_log()

            