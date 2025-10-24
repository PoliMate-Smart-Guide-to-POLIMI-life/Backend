from django.contrib import admin
from apps.questions.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "get_user_enrollment",
        "get_user_name",
        "get_user_email",
        "text",
    )

    search_fields = (
        "user__enrollment_number",
        "user__first_name",
        "user__last_name",
        "user__email",
        "text"
    )

    fieldsets = (
        ("User Information", {
            "fields": ("user",)
        }),
        ("Question Details", {
            "fields": ("text",)
        }),
    )

    def get_user_enrollment(self, obj):
        return obj.user.enrollment_number
    get_user_enrollment.short_description = "Enrollment Number"

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_name.short_description = "Name"

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = "Email"

    def has_add_permission(self, request):
        return False
