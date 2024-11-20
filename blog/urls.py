from django.urls import path
from blog.views import *

urlpatterns = [
    # path("", index, name="index"),
    # path("articles/<int:pk>/", article_detail, name="detail"),
    # path("category/<int:pk>/", get_articles_category, name="category"),
    path("", ArticleView.as_view(), name="index"),
    path("category/<int:pk>/", ArticleByCategory.as_view(), name="category"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="detail"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("add_comment/<int:article_id>/", save_comment, name="save_comment"),
    path("add_article/", AddArticle.as_view(), name="add_article"),
    path("edit_article/<int:pk>/", EditArticle.as_view(), name="edit_article"),
    path("delete_article/<int:pk>/", DeleteArticle.as_view(), name="delete_article"),
]