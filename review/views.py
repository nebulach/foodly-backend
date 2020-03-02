import json
from .models import Review

from products.models import Product
from account.models import User
from django.views import View
from django.http import HttpResponse, JsonResponse
from account.utils import login_check


class ReviewCreateView(View):
    @login_check
    def post(self, request, product_id):  # create
        data = json.loads(request.body)
        user_id = request.user
        # product_id = Product.objects.get(id = product_id)
        try:
            if Product.objects.filter(id=product_id).exists():
                if len(data['review']) != 0 or data['review'] is not None:
                    Review(
                        user_id=user_id,
                        review=data['review'],
                        product_id=product_id,
                    ).save()
                    review_data = Review.objects.all()
                    return JsonResponse({'message': list(review_data)}, status=200)

        except KeyError:
            return HttpResponse(status=400)
        except User.DoesNotExist:
            return HttpResponse(status=400)


class ReviewUpdateView(View):
    @login_check
    def post(self, request, product_id, review_id):
        data = json.load(request.body)
        print(data)  # id ,  user_id  , review , create_at  , update_at  , product_id
        try:
            review_data = Review.objects.get(id=review_id, product_id=product_id, user_id=request.user.id)

            if len(data) != 0 or data['review'] is not None:
                review_data.review = data['review']
                review_data.save()

                review_data = Review.objects.all()
                return JsonResponse({'message': list(review_data)}, status=200)
        except Review.DoesNotExist:
            return JsonResponse({'message': 'INVALD_REVIEW'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALD_USER"}, status=400)

    @login_check
    def delete(self, request, prodict_id, review_id):
        try:
            review_data = Review.objects.get(id=review_id, user_id=request.user.id)
            review_data.delete()
            review_data.save()

            review_data = Review.objects.all()
            return JsonResponse({"SECCESS": list(review_data)}, status=200)
        except:
            return HttpResponse(status=400)