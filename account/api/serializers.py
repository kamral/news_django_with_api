from  rest_framework import serializers
from account.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('email','password')
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user

