import csv
from config.database import connection

def load_data():
  
    with open('data/assets.csv', 'r', newline='', encoding='utf-8') as file:
        read_csv = csv.reader(file, delimiter=',', quotechar='"')
        next(read_csv)
     
        for row in read_csv:
            build={}
            build['build_status'] = row[0]
            build['is_active'] = row[1]
            build['start_month'] = row[2]
            build['construction_type'] = row[3]
            build['date_diff'] = row[4]
            build['description'] = row[5]
            build['date_in'] = row[6]
            build['property_type'] = row[7]
            build['end_week'] = row[8]
            build['typology_type'] = row[9]
            build['id'] = row[10]
            build['coordinates'] = row[11]
            build['boundary_id'] = row[12]
            build['id_uda'] = row[13]
            build['title'] = row[14]
            build['listing_type'] = row[15]
            build['date'] = row[16]
            connection.data.builds.insert_one(build) 
    return True