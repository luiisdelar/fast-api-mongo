def build_entity(data) -> dict:
    return {
        'build_status': data['build_status'],
        'is_active': data['is_active'],
        'start_month': data['start_month'],
        'construction_type': data['construction_type'],
        'date_diff': data['date_diff'],
        'description': data['description'],
        'date_in': data['date_in'],
        'property_type': data['property_type'],
        'end_week': data['end_week'],
        'typology_type': data['typology_type'],
        'id': data['id'],
        'coordinates': data['coordinates'],
        'boundary_id': data['boundary_id'],
        'id_uda': data['id_uda'],
        'title': data['title'],
        'listing_type': data['listing_type'],
        'date': data['date'],
    }

            
def builds_entity(entity) -> list:
    return [build_entity(item) for item in entity]