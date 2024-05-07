from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta,datetime
from base.models import PurchaseOrder,Vendor
from .models import HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def user_created(sender, instance, created, **kwargs):
    if not created:
        if instance:
            
            total_vendor_purchase_orders=PurchaseOrder.objects.filter(vendor=instance.vendor)
            total_vendor_purchase_orders_count=total_vendor_purchase_orders.count()
            time_differences_array = []
            #average_response_time
            for response_time in total_vendor_purchase_orders:
                 if response_time.acknowledgement_date is not None:                    
                    time_difference_for_acknowledge_date = response_time.acknowledgement_date - timedelta(days=3)
                    time_difference=time_difference_for_acknowledge_date- response_time.issue_date
                    time_differences_array.append(time_difference)

            if not len(time_differences_array)==0:
                total_time_difference = sum(td.total_seconds() for td in time_differences_array)
                average_time_difference_seconds = total_time_difference / len(time_differences_array) 
                average_hours = int(average_time_difference_seconds // 3600)
                average_minutes = int((average_time_difference_seconds % 3600) / 60)

                # average_days = int(average_time_difference_seconds // (24 * 3600))
                # remaining_seconds = int(average_time_difference_seconds % (24 * 3600))
                # average_hours = int(remaining_seconds // 3600)
                # remaining_seconds %= 3600
                # average_minutes = int(remaining_seconds // 60)
                # average_seconds = int(remaining_seconds % 60)
                    
                avg_response_time=str(average_hours)+"."+str(average_minutes)
            

            #fulfillment_rate
                if PurchaseOrder.objects.filter(vendor=instance.vendor,status='completed').exists():
                    completed_vendor_purchase_orders=PurchaseOrder.objects.filter(vendor=instance.vendor,status='completed')
                    completed_vendor_purchase_orders_count=completed_vendor_purchase_orders.count()
                    division=completed_vendor_purchase_orders_count/total_vendor_purchase_orders_count
                    multiplied_final_result=division*100

                #On-time deivery Rate
                    count=0
                    for purchase_delivery_date in completed_vendor_purchase_orders:
                        if purchase_delivery_date.delivery_date <= purchase_delivery_date.acknowledgement_date:
                            count+=1
                    
                    result_on_time_delivery=count/completed_vendor_purchase_orders.count()
                    result_on_time_delivery=result_on_time_delivery*100
                                        

                #quality_rating_avg
                    sum_of_quality_rating=0

                    for each_quality_rating in completed_vendor_purchase_orders:
                            sum_of_quality_rating+=each_quality_rating.quality_rating
                    
                    result_quality_rating=sum_of_quality_rating/completed_vendor_purchase_orders_count

            #instance saving
                    data=Vendor.objects.get(name=instance.vendor)
                    # data=HistoricalPerformance.objects.get(vendor=vendor_data)
                    data.fulfillment_rate=multiplied_final_result
                    data.quality_rating_avg=result_quality_rating
                    data.on_time_delivery_rate=result_on_time_delivery
                    data.average_response_time=avg_response_time
                    data.save()
                    HistoricalPerformance.objects.create(
                            vendor=instance.vendor,
                            date=datetime.now(),
                            quality_rating_avg=result_quality_rating,
                            on_time_delivery_rate=result_on_time_delivery,
                            average_response_time=avg_response_time,
                            fulfillment_rate=multiplied_final_result)
                else:
                    data=Vendor.objects.get(name=instance.vendor)
                    data.average_response_time=avg_response_time
                    data.save()
                    if HistoricalPerformance.objects.filter(vendor=instance.vendor).exists():
                        data=HistoricalPerformance.objects.filter(vendor=instance.vendor).order_by('-date').first()
                        HistoricalPerformance.objects.create(
                        vendor=instance.vendor,
                        date=datetime.now(),
                        quality_rating_avg=data.quality_rating_avg,
                        on_time_delivery_rate=data.on_time_delivery_rate,
                        average_response_time=avg_response_time,
                        fulfillment_rate=data.fulfillment_rate)
                    else:
                        HistoricalPerformance.objects.create(
                        vendor=instance.vendor,
                        date=datetime.now(),
                        quality_rating_avg=0,
                        on_time_delivery_rate=0,
                        average_response_time=avg_response_time,
                        fulfillment_rate=0)



                



        else:
            print("status is not changed to completed")

    elif created:
        if not HistoricalPerformance.objects.filter(vendor=instance.vendor).exists():
            HistoricalPerformance.objects.create(vendor=instance.vendor)
