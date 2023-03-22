# IMPORT MODULES
import csv
import json
import sys

class JSONGenerator:
    """Class to convert a .csv file to .json"""

    def __init__(self, filename: str) -> None:
        """Defines the constructor for a JSONGenerator object"""
        self.filename = filename
        self.headers = []
        self.json_strings = []

        self._convert_()

    def save_to_file(self, filename: str) -> None:
        """Saves a list of json strings to a .json file"""
        json_object = json.dumps(self.json_strings, indent=4)
        with open(filename, "w") as file:
            file.write(json_object)

    def _convert_(self) -> None:
        """Converts .csv data format to .json data format"""
        try:
            with open(self.filename, "r") as file:
                # READ FILE CONTENTS
                reader = csv.reader(file)

                for x,row in enumerate(reader):
                    if x == 0:
                        # GET FILE HEADERS
                        self.headers = row
                        del self.headers[0]
                    else:
                        del row[0]

                        entry_headers = []
                        entry_data = []
                        for y,_ in enumerate(row):
                            # ONLY KEEP ROWS THAT HAVE DATA
                            if len(row[y]) > 0:
                                entry_headers.append(self.headers[y])
                                entry_data.append(row[y])

                        json_string = {}
                        for z, header in enumerate(entry_headers):
                            # ADD ROW DATA TO JSON STRING
                            json_string[header] = entry_data[z]

                        self.json_strings.append(json_string)
        except FileNotFoundError:
            print("File Not Found: {}".format(self.filename))
            sys.exit(1)

    def get_json_strings(self) -> list:
        """Returns a list of JSON strings"""
        return self.json_strings

    def get_headers(self) -> list:
        """Returns a list of file headers"""
        return self.headers

if __name__ == "__main__":
    data_filename = "employee_list_cme.csv"
    save_to_filename = "employee_list_cme.json"

    generator = JSONGenerator(data_filename)
    print("Data in \"{}\" Successfully Converted to JSON format.".format(data_filename))
    generator.save_to_file(save_to_filename)
    print("JSON Data Saved to \"{}\".".format(save_to_filename))
