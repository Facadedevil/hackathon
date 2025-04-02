from django.db import models

class CallSummary(models.Model):
    audio_file = models.FileField(upload_to='audio/%Y/%m/%d/')
    transcription = models.JSONField(null=True, blank=True)
    summary = models.TextField()
    titles = models.JSONField(default=list)  # Changed from required to default empty list
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('processing', 'Processing'), 
                ('completed', 'Completed'), ('failed', 'Failed')],
        default='pending'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Summary {self.id} - {self.created_at}"