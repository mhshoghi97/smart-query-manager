from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import DeclarativeBase  # pyright: ignore[reportMissingImports]
from app.core.config import settings


class Base(DeclarativeBase):
    pass


# Async engine
engine = create_async_engine(settings.database_url, echo=settings.debug)

# Async session
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()