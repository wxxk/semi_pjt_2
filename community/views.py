from django.shortcuts import render, redirect, get_object_or_404
from .forms import QnaForm, ReviewForm, UpdateQnaForm, QnaForm_2, Qna_ReviewForm
from .models import QnA, Review, Photo
from products.models import Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_safe
from datetime import date, datetime, timedelta


# Create your views here.


def index(request):
    qna = QnA.objects.all().order_by("-pk")
    context = {"qna": qna}
    return render(request, "community/index.html", context)


# 상품에 대한 문의
@login_required
def qna_create(request, product_pk):
    if request.method == "POST":
        qna_form = QnaForm(request.POST, request.FILES)
        if qna_form.is_valid():
            qna = qna_form.save(commit=False)
            qna.user = request.user
            qna.Product = Products.objects.get(pk=product_pk)
            qna.save()
            return redirect("community:index")
    else:
        qna_form = QnaForm()
    context = {
        "qna_form": qna_form,
    }
    return render(request, "community/community_create.html", context)


# 상품이 아닌 일반적인 문의
@login_required
def qna(request):
    if request.method == "POST":
        print(1)
        qna_form = QnaForm_2(request.POST, request.FILES)
        if qna_form.is_valid():
            qna = qna_form.save(commit=False)
            qna.user = request.user
            qna.save()
            return redirect("community:index")

    else:
        qna_form = QnaForm_2()
    context = {
        "qna_form": qna_form,
    }
    return render(request, "community/qna_create.html", context)


@login_required
def qna_detail(request, qna_pk):
    qna = QnA.objects.get(pk=qna_pk)
    if (request.user == qna.user) or (request.user.is_staff):
        qna_hits = get_object_or_404(QnA, pk=qna_pk)
        qna_review_form = Qna_ReviewForm()
        qna_reviews = qna.qna_review_set.all()
        if qna_reviews:
            qna.solve = True
            qna.save()
        context = {
            "qna": qna,
            "qna_hits": qna_hits,
            "qna_review_form": qna_review_form,
            "qna_reviews": qna_reviews,
        }
        response = render(request, "community/qna_detail.html", context)
    else:
        return redirect("community:index")

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get("hitboard_1", "_")

    if f"_{qna_pk}_" not in cookie_value:
        cookie_value += f"{qna_pk}_"
        response.set_cookie(
            "hitboard_1", value=cookie_value, max_age=max_age, httponly=True
        )
        qna_hits.hits += 1
        qna_hits.save()
    return response


@login_required
def qna_update(request, qna_pk):
    qna = get_object_or_404(QnA, pk=qna_pk)
    if request.user == qna.user:
        if request.method == "POST":
            qna_form = UpdateQnaForm(request.POST, request.FILES, instance=qna)
            if qna_form.is_valid():
                qna = qna_form.save(commit=False)
                qna.user = request.user
                qna.save()
                messages.success(request, "수정 완료")
                return redirect("community:qna_detail", qna_pk)
        else:
            qna_form = UpdateQnaForm(instance=qna)
        context = {
            "qna_form": qna_form,
            "qna": qna,
        }
        return render(request, "community/community_create.html", context)
    else:
        messages.success(request, "작성자만 수정가 가능함")
        return redirect("community:qna_detail", qna_pk)


@login_required
def qna_delete(request, qna_pk):
    qna = get_object_or_404(QnA, pk=qna_pk)
    if request.user == qna.user:
        qna.delete()
        messages.success(request, "삭제 완료")
        return redirect("community:index")
    else:
        messages.success(request, "작성자만 삭제가 가능함")
        return redirect("community:index")


@login_required
def qna_password(request, qna_pk):
    qna = get_object_or_404(QnA, pk=qna_pk)
    if request.user.is_staff:
        return redirect("community:qna_detail", qna_pk)

    else:

        if request.method == "POST":
            if request.POST["password"] == qna.password:
                return redirect("community:qna_detail", qna_pk)

            else:
                return redirect("community:index")
        else:
            return render(request, "community/qna_password.html")


@login_required
def qna_review(request, qna_pk):
    if request.user.is_staff:
        qna_review_form = Qna_ReviewForm(request.POST)
        if qna_review_form.is_valid():
            qna_review = qna_review_form.save(commit=False)
            qna_review.QnA = QnA.objects.get(pk=qna_pk)
            qna_review.user = request.user
            qna_review.save()
            return redirect("community:qna_detail", qna_pk)


# 리뷰


def review_index(request):
    reviews = Review.objects.all()
    reviews_2 = Review.objects.all()
    print(reviews_2)
    context = {
        "reviews": reviews,
        "reviews_2": reviews_2,
    }
    return render(request, "community/review_index.html", context)


@login_required
def review_create(request, product_pk):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = Products.objects.get(pk=product_pk)
            review.save()
            for img in request.FILES.getlist("imgs"):
                photo = Photo()
                photo.review = review
                photo.image = img
                photo.save()
            return redirect("products:detail", product_pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "community/community_create.html", context)


def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    print(review)
    context = {
        "review": review,
    }
    return render(request, "community/review_detail.html", context)


@login_required
def review_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    photo = review.photo_set.all()
    if request.user == review.user:
        if request.method == "POST":
            photo.delete()
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()
                for img in request.FILES.getlist("imgs"):
                    photo = Photo()
                    photo.review = review
                    photo.image = img
                    photo.save()
                messages.success(request, "수정 완료")
                return redirect("products:detail", review.product_id)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            "review_form": review_form,
            "review": review,
            "photo": photo,
        }
        print(photo)
        return render(request, "community/community_create.html", context)
    else:
        messages.success(request, "작성자만 수정가 가능함")
        return redirect("community:review_detail", review_pk)


@login_required
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        messages.success(request, "삭제 완료")
        return redirect("community:review_index")
    else:
        messages.success(request, "작성자만 삭제가 가능함")
        return redirect("community:review_index")
