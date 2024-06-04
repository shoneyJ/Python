# from uuid import UUID

# from sqlalchemy import delete, select
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.ext.asyncio import AsyncSession

# from schemas import (
#    AppModel,
#    AppSchema,
#    User,
#    UserCreate
# )


# class SnippetException(Exception):
#     pass


# class IntegrityConflictException(Exception):
#     pass


# class NotFoundException(Exception):
#     pass


# def CrudFactory(model: AppModel):
#     class AsyncCrud:
#         @classmethod
#         async def create(
#             cls,
#             session: AsyncSession,
#             data: AppSchema,
#         ) -> AppModel:
#             """Accepts a Pydantic model, creates a new record in the database, catches
#             any integrity errors, and returns the record.

#             Args:
#                 session (AsyncSession): SQLAlchemy async session
#                 data (SnippetSchema): Pydantic model

#             Raises:
#                 IntegrityConflictException: if creation conflicts with existing data
#                 SnippetException: if an unknown error occurs

#             Returns:
#                 SnippetModel: created SQLAlchemy model
#             """
#             try:
#                 db_model = model(**data.model_dump())
#                 session.add(db_model)
#                 await session.commit()
#                 await session.refresh(db_model)
#                 return db_model
#             except IntegrityError:
#                 raise IntegrityConflictException(
#                     f"{model.__tablename__} conflicts with existing data.",
#                 )
#             except Exception as e:
#                 raise SnippetException(f"Unknown error occurred: {e}") from e

    
#     AsyncCrud.model = model
#     return AsyncCrud