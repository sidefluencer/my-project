import json
import csv
 
class FileManager:
    @staticmethod
    def export_to_csv(data_list, file_path):
        if isinstance(data_list, dict):
            data_list = [data_list]
        
        if len(data_list) == 0:
            return
        
        headrow = data_list[0].keys()
 
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headrow, delimiter=";")
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)
 
    @staticmethod
    def export_to_json(data_list, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4, default=str)
 
 
    @staticmethod
    def import_from_csv(file_path):
        data = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    data.append(row)
            return data
        except:
            return []