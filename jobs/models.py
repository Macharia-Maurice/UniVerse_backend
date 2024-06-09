from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class Job(models.Model):
    author = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="jobs", verbose_name=_("Job Owner"))
    title = models.CharField(_("Title") ,max_length=255)
    description = models.TextField(_("Description"))
    media = models.FileField(
    _("Job Media"),
    null=True, blank=True,
    upload_to="media/Job_Media",
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov', 'avi'])]
    )
    application_deadline = models.DateTimeField(_("Application Deadline"))
    application_procedure = models.TextField(_("Application Procedure"))
    created_at = models.DateTimeField(_("Created At"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Created At"),auto_now=True)


    def __str__(self):
        return self.title

    def is_application_open(self):
        return timezone.now() < self.application_deadline

    def extend_deadline(self, new_deadline):
        if new_deadline > self.application_deadline:
            self.application_deadline = new_deadline
            self.save()
        else:
            raise ValueError(_("New deadline must be later than the current deadline."))
