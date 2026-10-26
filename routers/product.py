from fastapi import APIRouter
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

# 5. Create API operation

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.get('/all')
def get_all_products():
    # return products

    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get('/{id}')
def get_product(id: int):

    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center
            }}
            </style>
            <div class="product">{product}</div>
        </head>
        """

    return HTMLResponse(content=out, media_type="text/html")

### Why do we need Custom Responces?
# 1. add parameters: Headers, Cookies
# 2. different types of response i.e plain text, xml, html, files, streaming
# 3. complex decisional logic
# 4. better docs