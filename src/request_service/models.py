
from django_mysql.models import JSONField
from django.db.models import (
                                CharField,
                                DateField,
                                BooleanField,
                                Model,
                            )


class Service(Model):
    requester = CharField(max_length=31, default='', editable=True)
    request_date = DateField("date requested")
    active = BooleanField(default=True)
    payload = JSONField(null=True)

    class Meta:
        db_table = "Service"
        get_latest_by = 'request_date'
        ordering = ["-request_date", "requester"]

    def __str__(self):
        date_string = self.request_date.strftime("%Y-%m-%d")
        return f"{self.requester} on {date_string}"

