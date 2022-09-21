"""
Admin site configurations for integrated channel's Content Metadata Transmission table.
"""

from django.contrib import admin

from integrated_channels.integrated_channel.models import ContentMetadataItemTransmission


@admin.register(ContentMetadataItemTransmission)
class ContentMetadataItemTransmissionAdmin(admin.ModelAdmin):
    """
    Admin for the ContentMetadataItemTransmission audit table
    """
    list_display = (
        'enterprise_customer',
        'integrated_channel_code',
        'content_id',
        'api_response_status_code',
        'remote_deleted_at',
        'modified'
    )

    search_fields = (
        'enterprise_customer__name',
        'enterprise_customer__uuid',
        'integrated_channel_code',
        'content_id'
    )

    raw_id_fields = (
        'enterprise_customer',
    )

    list_per_page = 1000
