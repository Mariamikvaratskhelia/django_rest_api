from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemSerializer

@api_view(['GET', 'POST', 'DELETE'])
def item_list_create(request):
    if request.method == 'GET':
        items = Items.objects.all()
        item_list = []

        for item in items:
            item_data = {
                'id':item.id,
                'name': item.name,
                'description':item.description,
                'price': item.price,
                'created_at': item.created_at,
                'is_active': item.is_active,
                'quantity': item.quantity,
                'category': item.category,
            }
            item_list.append(item_data)

        return Response({'items': item_list})
    elif request.method == 'POST':
        data = request.data
        serializer = ItemSerializer(data = data)
        if serializer.is_valid():
            item = serializer.save()
            new_item = Items.objects.create(
                name=data.get("name"),
                description=data.get("description"),
                price=data.get("price"),
                quantity=data.get("quantity"),
                category=data.get("category"),
            
            )

            return Response({"new product": {
                'id': new_item.id,
                'name': new_item.name,
                'description': new_item.description,
                'price': new_item.price,
                'created_at': new_item.created_at,
                'is_active': new_item.is_active,
                'quantity': new_item.quantity,
                'category': new_item.category,
            }}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def item_delete(request, id):
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return Response(
            {"error": "Item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    item.delete()
    return Response(
        {"message": "Item deleted successfully"},
        status=status.HTTP_200_OK
    )
