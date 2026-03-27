from __future__ import annotations

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class RouteSegment(Base):
    __tablename__ = "route_segments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    segment_index: Mapped[int] = mapped_column(Integer)
