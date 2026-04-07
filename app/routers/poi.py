from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
from typing import Optional
from ..database import SessionLocal
from .. import models
from ..utils import calculate_distance

router = APIRouter(prefix="/pois", tags=["POIs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_pois(
    page: int = Query(1, gt=0),
    limit: int = Query(10, gt=0),
    search: Optional[str] = None,
    categories: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    radius: Optional[float] = None,
    db: Session = Depends(get_db)
):
    if (lat or lng or radius) and not (lat and lng and radius):
        raise HTTPException(400, "lat, lng and radius must be provided together")

    query = db.query(models.POI).options(
        joinedload(models.POI.location),
        joinedload(models.POI.category)
    )

    if search or categories:
        query = query.join(models.Category)

    if search:
        query = query.filter(
            or_(
                models.POI.name.ilike(f"%{search}%"),
                models.Category.name.ilike(f"%{search}%")
            )
        )

    if categories:
        cats = [c.strip() for c in categories.split(",")]
        query = query.filter(models.Category.name.in_(cats))

    pois = query.all()
    if not pois:
        raise HTTPException(404, "No POIs found")

    if lat and lng and radius:
        pois = [
            p for p in pois
            if p.location and calculate_distance(
                lat, lng, p.location.latitude, p.location.longitude
            ) <= radius
        ]
        if not pois:
            raise HTTPException(404, "No POIs found within radius")

    total = len(pois)
    start = (page - 1) * limit
    paginated = pois[start:start + limit]
    if not paginated:
        raise HTTPException(404, "Page out of range")

    result = [
        {
            "type": "Feature",
            "properties": {
                "id": p.id,
                "name": p.name,
                "category": p.category.name if p.category else None,
                "description": p.description
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    p.location.longitude if p.location else None,
                    p.location.latitude if p.location else None
                ]
            }
        } for p in paginated
    ]

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": result
    }


@router.get("/{poi_id}")
def get_poi(poi_id: int, db: Session = Depends(get_db)):
    if poi_id <= 0:
        raise HTTPException(400, "Invalid POI ID")

    poi = db.query(models.POI).options(
        joinedload(models.POI.location),
        joinedload(models.POI.category)
    ).filter(models.POI.id == poi_id).first()

    if not poi:
        raise HTTPException(404, "POI not found")

    return {
        "type": "Feature",
        "properties": {
            "id": poi.id,
            "name": poi.name,
            "category": poi.category.name if poi.category else None,
            "description": poi.description
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                poi.location.longitude if poi.location else None,
                poi.location.latitude if poi.location else None
            ]
        }
    }