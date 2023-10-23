from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


class Profile(models.Model):

    CAN_SELECT_ANOTHER_USER = 'Pode selecionar outro usuário'

    CUSTOM_PERMISSIONS = (
        (CAN_SELECT_ANOTHER_USER, 'CSAU'), 
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(
        'Data de nascimento',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        'Foto',
        upload_to='users/%Y/%m/%d/',
        blank=True
    )
    is_active = models.BooleanField(
        'Ativo',
        default=True
    )

    have_dependents = MultiSelectField('Permissões Customizadas', 
                                       choices=CUSTOM_PERMISSIONS,
                                       max_length=50,
									   blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    


