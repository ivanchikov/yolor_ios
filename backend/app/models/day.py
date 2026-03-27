from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Day(Base):
    __tablename__ = "days"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    day_index: Mapped[int] = mapped_column(Integer)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"))
    trip: Mapped["Trip"] = relationship(back_populates="days")
    stops: Mapped[list["Stop"]] = relationship(
        back_populates="day",
        cascade="all, delete-orphan",
    )
