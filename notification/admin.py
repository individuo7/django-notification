from django.contrib import admin

from notification.models import NoticeType, NoticeSetting, NoticeQueueBatch, Email


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "send"]


class EmailAdmin(admin.ModelAdmin):
    """
    Admin part for managing the the Email model
    """
    list_display = ['sent', 'to', 'subject', 'notice_type']
    list_filter = ['notice_type','sent',]
    readonly_fields = ['sent', 'to', 'subject', 'body', 'notice_type']
    search_fields = ['subject', 'body', 'to', 'notice_type']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Email, EmailAdmin)
admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
