from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        self.before_save()
        self.full_clean()
        super().save()
        self.after_save()

    def delete(self):
        self.before_delete()
        try:
            return super().delete()
        finally:
            self.after_delete()

    def before_save(self):
        pass

    def after_save(self):
        pass

    def before_delete(self):
        pass

    def after_delete(self):
        pass

    class Meta:
        abstract = True
