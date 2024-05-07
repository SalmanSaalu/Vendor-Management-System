from rest_framework import serializers
from .models import Vendor, PurchaseOrder,HistoricalPerformance
from rest_framework.exceptions import ValidationError
import random
import json
import datetime
from datetime import timedelta

# from rest_framework_simplejwt.tokens import RefreshToken


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        # vendor_code2=serializers.SerializerMethodField()
        fields = [
            "id",
            "name",
            "contact_details",
            "address",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]

        read_only_fields = ["vendor_code"]

    def create(self, validated_data):
        vendorcode = random.randint(10000, 99999)
        vendor = Vendor.objects.create(**validated_data, vendor_code=vendorcode)
        return vendor


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgement_date",
        ]

        read_only_fields = [
            "po_number",
            "order_date",
            "delivery_date",
            "issue_date",
            "acknowledgement_date",
            "quantity",
            "quality_rating"
        ]

    def create(self, validated_data):
        try:
            vendor = validated_data.get("vendor")
            if vendor is None:
                raise serializers.ValidationError("Vendor is required.")
            
            if validated_data.get("status")!='pending':
                raise serializers.ValidationError("Please give status pending.")

            randomNumber1 = random.randint(1000, 9999)
            randomNumber2 = random.randint(1000, 9999)
            po_number = str(randomNumber1) + str(randomNumber2)
            print(validated_data)
            input_string = validated_data["items"]
            input_string = input_string.replace("'", '"')
            json_data = json.loads(input_string)
            validated_data["items"] = json_data
            quantity = len(json_data)
            current_datetime = datetime.datetime.now()
            issue_date = current_datetime + timedelta(minutes=1)

            vendor = PurchaseOrder.objects.create(
                **validated_data,
                po_number=po_number,
                quantity=quantity,
                order_date=current_datetime,
                issue_date=issue_date
            )
            return vendor
        except:
            raise serializers.ValidationError("please give inputs in a correct format")

class PurchaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgement_date",
        ]

        read_only_fields = [
            "items",
            "po_number",
            "order_date",
            "delivery_date",
            "issue_date",
            "acknowledgement_date",
            "quantity",
        ]

    def update(self, instance, validated_data):
        if instance.status=="completed":
            raise serializers.ValidationError("Your Purchase order is already delivered cannot be updated")
        elif validated_data['status'] not in ['completed','pending','canceled']:
            raise serializers.ValidationError("please give status as 'completed' or 'pending' or 'canceled'")
        elif instance.acknowledgement_date is None:
            instance.vendor=validated_data.get("vendor",instance.vendor)
        
        quality_rating = validated_data.get("quality_rating")
        if quality_rating is None:
            raise serializers.ValidationError("quality rating is required when status is completed.")
        elif validated_data['status']=='completed':
            if validated_data['quality_rating'] > 5 or validated_data['quality_rating']<0:
                raise serializers.ValidationError("please give quality rating lesser than  5 and greater than 0")

            
            if instance.acknowledgement_date is None:
                    current_datetime=datetime.datetime.now()
                    instance.acknowledgement_date=current_datetime + timedelta(days=3)
     
            
            instance.status = validated_data.get("status", instance.status)
            instance.quality_rating = validated_data.get(
                "quality_rating", instance.quality_rating
            )

            instance.delivery_date=datetime.datetime.now()
            instance.save()
            return instance
        
        else:
            instance.status = validated_data.get("status", instance.status)
            instance.vendor = validated_data.get("vendor",instance.vendor)
            instance.save()
            return instance

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = [
            "id",
            "vendor",
            "fulfillment_rate",
            "average_response_time",
            "quality_rating_avg",
            "on_time_delivery_rate"
        ]