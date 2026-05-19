from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404

from .models import Produkt, Objednavka, Recenze, User
from .schemas import ReviewOut, ReviewIn, OrderOut, MessageSchema

api = NinjaAPI()

# ---------- Review endpoints ----------

@api.get("/products/{product_id}")
def get_product(request, product_id: int):
    product = get_object_or_404(Produkt, pk=product_id)

    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
    }

@api.get("/products/{product_id}/reviews", response=List[ReviewOut], tags=["reviews"])
def list_reviews(request, product_id: int):
    reviews = Recenze.objects.filter(product_id=product_id).select_related("user")

    return [
        {
            "id": r.id,
            "product_id": r.product_id,
            "user": r.user.name,
            "rating": r.rating,
            "comment": r.comment,
            "created_at": r.created_at.isoformat(),
        }
        for r in reviews
    ]


@api.post("/products/{product_id}/reviews", response={201: ReviewOut, 404: MessageSchema}, tags=["reviews"])
def create_review(request, product_id: int, payload: ReviewIn):
    product = get_object_or_404(Produkt, pk=product_id)
    user = get_object_or_404(User, pk=payload.user_id)

    review = Recenze.objects.create(
        product=product,
        user=user,
        rating=payload.rating,
        comment=payload.comment,
    )

    return 201, {
        "id": review.id,
        "product_id": review.product_id,
        "user": review.user.name,
        "rating": review.rating,
        "comment": review.comment,
        "created_at": review.created_at.isoformat(),
    }


# ---------- Order endpoints ----------


@api.get("/orders/{order_id}", response={200: OrderOut, 404: MessageSchema}, tags=["orders"])
def get_order(request, order_id: int):
    try:
        order = Objednavka.objects.select_related("user").prefetch_related("items__product").get(pk=order_id)
    except Objednavka.DoesNotExist:
        return 404, {"message": "Order not found."}

    return {
        "id": order.id,
        "user": order.user.name,
        "created_at": order.created_at.isoformat(),
        "items": [
            {
                "product_id": item.product.id,
                "product_name": item.product.name,
                "quantity": item.quantity,
            }
            for item in order.items.all()
        ],
    }