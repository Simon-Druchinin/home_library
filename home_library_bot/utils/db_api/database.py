from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URI

db = Gino()

async def create_db():
    # Make a connection with db
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor