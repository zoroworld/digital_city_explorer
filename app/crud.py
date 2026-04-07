from sqlalchemy.orm import Session
from . import models

def get_pois(db: Session, search=None, categories=None):
    query = db.query(models.POI)

    # 🔍 Search
    if search:
        query = query.filter(models.POI.name.ilike(f"%{search}%"))

    # 📂 Multiple categories
    if categories:
        cats = [c.strip() for c in categories.split(",")]
        query = query.filter(models.POI.category.in_(cats))

    return query.all()


def get_poi_by_id(db: Session, poi_id: int):
    return db.query(models.POI).filter(models.POI.id == poi_id).first()