from hashlib import md5

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')
    contact = serializers.SerializerMethodField()
    sys_url = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    def get_contact(self, user):
        return f'https://u.internal.myteam.mail.ru/profile/{user.email}'

    def get_sys_url(self, user):
        return f'https://home.vk.team/users/{user.username}'

    def get_avatar(self, user):
        if not user.email:
            return ''
        email_md5 = md5(user.email.lower().strip().encode()).hexdigest() if user.email else '0' * 32
        return f'https://home.vk.team/avatar/{email_md5}.jpg?s=150'

    class Meta:
        model = User
        fields = ('sys_id', 'username', 'name', 'contact', 'sys_url', 'avatar')
