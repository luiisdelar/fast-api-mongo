from pydantic import BaseModel

class Build(BaseModel):
    build_status: str
    is_active: str 
    start_month: str 
    construction_type: str 
    date_diff: str 
    description: str 
    date_in: str 
    property_type: str 
    end_week: str 
    typology_type: str 
    id: str 
    coordinates: str
    boundary_id: str 
    id_uda: str 
    title: str 
    listing_type: str 
    date: str 
