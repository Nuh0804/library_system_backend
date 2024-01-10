from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, empty
from django.core.exceptions import ValidationError
from .models import *


class OrderbookSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['user','collection', 'book', 'date_taken', 'date_to_return']

 
    def create(self, validated_data):
        book_requested = validated_data['book']
        collection = validated_data['collection']
        user = self.context['request'].user

        order = Order.objects.filter(book_id = book_requested, user_id = user)

        if order:
            raise serializers.ValidationError('you already ordered the book')
        if book_requested.is_taken:
            raise serializers.ValidationError('The book is already taken')
        elif collection.count <2:
            raise serializers.ValidationError('The books are not available')
        collection.count-=1
        collection.save()
        book_requested.is_taken = True
        book_requested.save()
        validated_data['user'] = user
        return  Order.objects.create(**validated_data)
    

    def validate(self, data):
        instance = Order(**data)
        try:
            instance.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        
        return data



class ReturnedBookSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=CurrentUserDefault())
    class Meta:
        model = Returned
        fields = ['user', 'order', 'date_returned']

    def create(self, validated_data):
        user_order = validated_data['order']
        user = validated_data['user']

        order = Order.objects.filter(id = user_order.id, user_id = user)
        if not order:
            raise serializers.ValidationError('incorrect order')

        user_order.is_returned = True
        book = user_order.book
        book.is_taken = False
        book.save()
        user_order.save()
        return Returned.objects.create(**validated_data)
    

    def __init__(self, *args, **kwargs):
        order_queryset = kwargs.pop('order_queryset', None)
        super(ReturnedBookSerializer, self).__init__(*args, **kwargs)

        # Customize the queryset for the 'author' field based on the current user's orders
        if order_queryset is not None:
            self.fields['order'].queryset = order_queryset

    def validate(self, data):
        instance = Returned(**data)
        try:
            instance.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        
        return data