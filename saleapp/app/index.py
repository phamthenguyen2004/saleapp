from flask import render_template, request
import dao
from app import db, app


@app.route("/")
def index():
    cates = dao.load_categories()
    prods = dao.load_products()
    return render_template("index.html", categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Desktop')
        # c3 = Category(name='Tablet')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

    products = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 3
    }, {
        "id": 4,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 4
    }, {
        "id": 5,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 5
    }]

    for p in products:
        prod = Products(**p)
        db.session.add(prod)

    db.session.commit()
