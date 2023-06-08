from app.api.dependencies import get_db
import app.models as models

def test_get_db():
    """Test if the db is reachable"""
    db = next(get_db())
    assert db
    assert db.execute('SELECT 1')


def test_alembic():
    """Test if the alembic has properly initialized tables"""
    db = next(get_db())
    try:
        db.query(models.Organisatie).all()
    except Exception:
        assert False