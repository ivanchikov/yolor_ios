from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Stop(Base):
    __tablename__ = "stops"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_index: Mapped[int] = mapped_column(Integer)
    poi_id: Mapped[str] = mapped_column(String(255))
    locked: Mapped[bool] = mapped_column(Boolean, default=False)
    day_id: Mapped[int] = mapped_column(ForeignKey("days.id"))
    day: Mapped["Day"] = relationship(back_populates="stops")
