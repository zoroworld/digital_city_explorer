# Digital City Explorer Application

## Over view Project

The backend provides map-related data by storing Points of Interest (POIs) with latitude and longitude. It supports basic spatial queries using a distance-based approach, where POIs within a given radius from a location are retrieved. The Haversine formula is used to calculate the great-circle distance between coordinates, ensuring accurate results. Additional features include filtering, search, pagination, and GeoJSON-based responses for map integration.

Logic on Haversine formula

The Haversine formula calculates the great-circle distance (shortest distance over the Earth’s surface) between two points given their latitude and longitude in degrees.



## Class diagram

POI class

    - id: int          
    - name: str        
    - description: str 
    - category_id: int 
    - location_id: int

    + category: Category
    + location: Location

location class      

    - id: int          
    - latitude: float  
    - longitude: float 

    + poi: POI      


Category class       

    - id: int          
    - name: str        

    + pois: List[POI]     

Relation with class

    category and POi relation is 1:M
    location and POI relation is 1:1


## API DESIGN

1. Endpoint

        GET /pois

        Discription:
        List all POIs (with search, category, radius, pagination)	

        Example:-
        1. /api/v1/pois?search=park&categories=park,shopping&page=1&limit=10

        2.  /api/v1/pois?search=park
        3.  /api/v1/pois?categories=park,shopping
        4.  /api/v1/pois?page=1&limit=10
        5. /api/v1/pois?lat=22.5726&lng=88.3639&radius=5

2. Endpoint 

        Discription
        Get POI by ID


        Example:
        http://127.0.0.1:8000/api/v1/pois/2


## Setup

- Clone the project

        git clone <your-repo-url>
        cd pois_app
        
- create python virtual enviroment

        # Create venv
        python3 -m venv .venv

        # Activate venv
        source .venv/bin/activate   # Linux/macOS
        # OR
        .venv\Scripts\activate      # Windows

- Install dependencies

        pip install -r requirements.txt

- Run the FastAPI server

        uvicorn app.main:app --reload

- Then open sqlite import the sql file pois.db.sql and  not make new database.

- the data will imported in sqlite and you can see apis.

- Test Api (openAPI or swagger)

        http://127.0.0.1:8000/docs
