from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from .constants import PREVIEW_LEN

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("Слаг", unique=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField("Текст поста")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(
        "Картинка", upload_to="posts/", blank=True, null=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        blank=True,
        verbose_name="Группа",
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text[:PREVIEW_LEN]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    text = models.TextField("Текст комментария")
    created = models.DateTimeField(
        "Дата создания", auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return (
            f"Комментарий {self.id} к посту {self.post_id} от {self.author}: "
            f"{self.text[:PREVIEW_LEN]}"
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "following"),
                name="unique_user_following",
            )
        ]

    def clean(self):
        if self.user == self.following:
            raise ValidationError("Нельзя подписаться на самого себя")

    def __str__(self):
        return f"{self.user} -> {self.following}"
