from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, BigInteger


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    ds_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(16))

    def __repr__(self):
        return f"User(id={self.id!r}, ds_id={self.ds_id!r}, name={self.name!r}, verified={self.verified!r})"


class Sponsor(Base):
    __tablename__ = "sponsors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ds_id: Mapped[int] = mapped_column(BigInteger)
    minecraft_name: Mapped[str] = mapped_column(String(16), )
    sponsor_role: Mapped[int]  = mapped_column(BigInteger)
    own_role: Mapped[int] = mapped_column(BigInteger, default=-1)
    mine_bonuses_status: Mapped[int] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return (f"User(id={self.id!r}, ds_id={self.ds_id!r}, minecraft_name={self.minecraft_name!r}," +
                f" sponsor_role={self.sponsor_role!r}, own_role={self.own_role!r}, " +
                f"mine_bonuses_status{self.mine_bonuses_status!r})")
