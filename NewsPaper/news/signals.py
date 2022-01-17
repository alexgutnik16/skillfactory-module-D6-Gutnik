from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Post


@receiver(m2m_changed, sender=Post.post_category.through)
def notify_subscribers(sender, instance, **kwargs):
    text = instance.text[:50] + '...'
    for category in instance.post_category.all():
        for user in category.subscribers.all():
            send_mail(
                subject=f'Привет, {user.username}, новый пост в категории {category.category_name}!',
                message=text,
                from_email='alexvgutnik@yandex.ru',
                recipient_list=[user.email],
                )
