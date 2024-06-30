from django.contrib import admin

from apps.emails.models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ["subject", "to", "_status", "sent_at"]
    actions = ["send_email"]

    def get_queryset(self, request):
        """
        We want to defer the `html` and `plain_text` fields,
        since we are not showing them in the list & we don't need to fetch them.

        Potentially, those fields can be quite heavy.
        """
        queryset = super().get_queryset(request)
        return queryset.defer("html", "plain_text")

    def _status(self, obj):
        match obj.status:
            case Email.Status.SENT:
                return "✅ " + Email.Status.SENT
            case Email.Status.FAILED:
                return "❌ " + Email.Status.FAILED
            case Email.Status.SENDING:
                return "📩 " + Email.Status.SENDING
            case _:
                return "❓ " + Email.Status.READY
