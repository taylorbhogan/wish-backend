from django.db import models

class Group(models.Model):
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.code

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    hashed_password = models.TextField()
    avatar = models.TextField(blank=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "groups": self.groups
            }

class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.TextField(blank=True)
    wished_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wished_by')
    claimed_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='claimed_by')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "wished_by": self.wished_by,
            "claimed_by": self.claimed_by,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
            }
