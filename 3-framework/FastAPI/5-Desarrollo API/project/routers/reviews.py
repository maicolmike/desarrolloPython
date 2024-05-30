from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from ..database import User
from ..database import Movie
from ..database import UserReview

#from ..common import get_current_user

from ..schemas import ReviewRequestModel
from ..schemas import ReviewResponseModel
from ..schemas import ReviewRequestPutModel

router = APIRouter(prefix='/reviews')
# crear nueva reseña
@router.post('',response_model = ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):

    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code = 404, detail = 'User not found')
    
    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code = 404, detail = 'Movie not found')
    
    user_review = UserReview.create(
        user_id = user_review.user_id,
        movie_id = user_review.movie_id,
        review = user_review.review,
        score = user_review.score
    )

    return user_review

# listado de reseñas
@router.get('', response_model = List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
    #reviews= UserReview.select() # select * from user_reviews
    reviews= UserReview.select().paginate(page,limit)

    return [user_review for user_review in reviews]

# obtener reseña
@router.get('/{review_id}', response_model = ReviewResponseModel)
async def get_review(review_id:int):
    #return review_id
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None : 
        raise HTTPException (status_code= 404, detail ='Review not found')
    
    return user_review
#actualizar reseñas
@router.put('/{review_id}',response_model = ReviewResponseModel)
async def update_review(review_id:int, review_request:ReviewRequestPutModel):
    #return review_id
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None : 
        raise HTTPException (status_code= 404, detail ='Review not found')
    
    user_review.review = review_request.review
    user_review.score = review_request.score

    user_review.save()

    return user_review

# eliminar reseñas
@router.delete('/{review_id}',response_model = ReviewResponseModel)
async def delete_review(review_id:int):
    #return review_id
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None : 
        raise HTTPException (status_code= 404, detail ='Review not found')
    
    user_review.delete_instance()

    return user_review