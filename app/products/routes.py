from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.products.models import Category, Product
from app.products.schemas import CategoryRequest, ProductRequest
from app.utils.security import get_current_user

products_router = APIRouter()

# Categories
@products_router.post("/categories")
def create_category(
    category: CategoryRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    category_exists = (
        db.query(Category)
        .filter(Category.name == category.name, Category.user_id == current_user.id)
        .first()
    )
    if category_exists:
        raise HTTPException(status_code=400, detail="Category already exists")
    new_category = Category(name=category.name, user_id=current_user.id)
    db.add(new_category)
    db.commit()
    return {"msg": "Category created successfully"}

@products_router.get("/categories")
def get_categories(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    return db.query(Category).filter(Category.user_id == current_user.id).all()

# Products
@products_router.post("/products")
def create_product(
    product: ProductRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    category = (
        db.query(Category)
        .filter(Category.id == product.category_id, Category.user_id == current_user.id)
        .first()
    )
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category_id=product.category_id,
        user_id=current_user.id,
    )
    db.add(new_product)
    db.commit()
    return {"msg": "Product created successfully"}

@products_router.get("/products")
def get_products(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    return db.query(Product).filter(Product.user_id == current_user.id).all()