from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        self.before_save()
        self.full_clean()
        super().save(**kwargs)
        self.after_save()

    def delete(self, **kwargs):
        self.before_delete()
        try:
            return super().delete(**kwargs)
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
