from app.models import Category, Products


def load_categories():
    return Category.query.order_by('id').all()

def load_products(cate_id=None):
    query = Products.query

    if cate_id:
    return query.all()
