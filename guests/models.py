# from __future__ import unicode_literals
import uuid

# from django.db import models

# # TODO: Change allowed types
# ALLOWED_TYPES = [
#     ('formal', 'formal'),
#     ('fun', 'fun'),
# ]

# # TODO: Change meals
# MEALS = [
#     ('beef', 'cow'),
#     ('fish', 'fish'),
#     ('hen', 'hen'),
#     ('vegetarian', 'vegetable'),
# ]

# LANGUAGES = [
#     ('en', 'English'),
#     ('da', 'Danish'),
#     ('vn', 'Vietnamese')
# ]


def _random_uuid():
    return uuid.uuid4().hex


# class Party(models.Model):
#     """A party consists of one or more guests"""
#     id = models.BigAutoField(primary_key=True)
#     name = models.TextField()
#     type = models.CharField(max_length=10, choices=ALLOWED_TYPES)
#     language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
#     category = models.CharField(max_length=20, null=True, blank=True)
#     save_the_date_sent = models.DateTimeField(null=True, blank=True, default=None)
#     save_the_date_opened = models.DateTimeField(null=True, blank=True, default=None)
#     invitation_id = models.CharField(max_length=32, db_index=True, default=_random_uuid, unique=True)
#     invitation_sent = models.DateTimeField(null=True, blank=True, default=None)
#     invitation_opened = models.DateTimeField(null=True, blank=True, default=None)
#     is_invited = models.BooleanField(default=False)
#     rehearsal_dinner = models.BooleanField(default=False)
#     is_attending = models.BooleanField(null=True, default=None)
#     comments = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f'Party: {self.name}'

#     @classmethod
#     def in_default_order(cls):
#         return cls.objects.order_by('category', '-is_invited', 'name')

#     @property
#     def ordered_guests(self):
#         return self.guest_set.order_by('is_child', 'pk')

#     @property
#     def num_guests(self) -> int:
#         return self.guest_set.count()

#     @property
#     def is_singular(self) -> bool:
#         return self.num_guests == 1

#     @property
#     def any_guests_attending(self) -> bool:
#         return any(self.guest_set.values_list('is_attending', flat=True))

#     @property
#     def guest_emails(self):
#         return list(filter(None, self.guest_set.values_list('email', flat=True)))


# class Guest(models.Model):
#     """A single guest"""
#     id = models.BigAutoField(primary_key=True)
#     party = models.ForeignKey(Party, on_delete=models.CASCADE)
#     first_name = models.TextField()
#     last_name = models.TextField(null=True, blank=True)
#     email = models.TextField(null=True, blank=True)
#     is_attending = models.BooleanField(null=True, default=None)
#     meal = models.CharField(max_length=20, choices=MEALS, null=True, blank=True)
#     is_child = models.BooleanField(default=False)

#     @property
#     def name(self):
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def language(self):
#         return self.party.language

#     @property
#     def unique_id(self):
#         # convert to string so it can be used in the "add" templatetag
#         return str(self.pk)

#     def __str__(self):
#         return f'Guest: {self.name}'
