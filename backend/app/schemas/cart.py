from pydantic import BaseModel,  Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description='Product ID')
    quantity: int = Field(..., gt=0, description='Quantity')
    
class CartItemCreate(CartItemBase):
    pass 

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description='Product ID')
    quantity: int = Field(..., gt=0, description='New quantity')
    
class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description='Product name')
    price: float = Field(..., description='Product price')
    quantity: int = Field(...)
    subtotal: float = Field(...)
    image_url: Optional[str] = Field(None)
    
class CartResponse(BaseModel):
    items: list[CartItem] = Field(...)
    total: float = Field(..., description='total')
    items_count: int = Field(..., description='total number of quantity')
    
    
         