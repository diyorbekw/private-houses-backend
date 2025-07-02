from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .study_info import StudyInfo
    from .passport_data import PassportData

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    study_info_id: Mapped[int] = mapped_column(ForeignKey("study_info.id"), nullable=False)
    passport_data_id: Mapped[int] = mapped_column(ForeignKey("passport_data.id"), nullable=False)

    study_info: Mapped["StudyInfo"] = relationship("StudyInfo", back_populates="application")
    passport_data: Mapped["PassportData"] = relationship("PassportData", back_populates="application")

    def __repr__(self):
        return (
            f"<Application(id={self.id}, study_info_id={self.study_info_id}, "
            f"passport_data_id={self.passport_data_id})>"
        )

    def __str__(self):
        return (
            f"Application #{self.id} — "
            f"StudyInfo ID: {self.study_info_id}, PassportData ID: {self.passport_data_id}"
        )
