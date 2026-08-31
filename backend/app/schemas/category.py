from pydantic import BaseModel, Field 

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=255, description="Имя товара")
    slug: str = Field(..., min_length=5, max_length=255, description='Слаг товара')

class CategoryCreate(CategoryBase):
    pass 

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category indentify')
    
    class Config:
        form_attributes = True


