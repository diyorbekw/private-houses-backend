from sqlalchemy.orm import Mapped, mapped_column , relationship
from sqlalchemy import String
from src.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.study_info import StudyInfo


class StudyDirection(Base):
    __tablename__ = "study_directions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    study_form: Mapped[str] = mapped_column(String(50), nullable=False)
    contract_sum: Mapped[str] = mapped_column(String(50), nullable=False)
    education_years: Mapped[str] = mapped_column(String(20), nullable=False)
    study_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    study_infos: Mapped[list["StudyInfo"]] = relationship("StudyInfo", back_populates="study_direction")

    def __repr__(self):
        return (
            f"<StudyDirection(id={self.id}, name='{self.name}', study_form='{self.study_form}', "
            f"contract_sum='{self.contract_sum}', education_years='{self.education_years}', "
            f"study_code='{self.study_code}')>"
        )
