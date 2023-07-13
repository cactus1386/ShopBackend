# from django.http import JsonResponse
# from .serializers import ProductSerializer, ImagesSerializer

# def create_product_with_images(request):
#     # Create a product
#     product_data = {
#         'name': 'Example Product',
#         'typeid': 1,
#         'price': 100,
#         'discount': 10,
#         'pic': 'example.jpg',
#         'count': 10,
#         'material': 'Example Material',
#         'brand': 'Example Brand',
#         'description': 'Example Description',
#     }

#     product_serializer = ProductSerializer(data=product_data)
#     if product_serializer.is_valid():
#         product = product_serializer.save()  # Save the product object
#     else:
#         return JsonResponse(product_serializer.errors, status=400)

#     # Create images associated with the product
#     image_data = [
#         {'product': product.id, 'image': 'image1.jpg'},
#         {'product': product.id, 'image': 'image2.jpg'},
#     ]

#     image_serializer = ImagesSerializer(data=image_data, many=True)
#     if image_serializer.is_valid():
#         image_serializer.save()  # Save the image objects with the associated product
#     else:
#         return JsonResponse(image_serializer.errors, status=400)

#     return JsonResponse(product_serializer.data, status=201)
