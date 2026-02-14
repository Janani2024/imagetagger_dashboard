from django.contrib import admin

from .models import Annotation, AnnotationType, SuperAnnotationType, Export, Verification, ExportFormat


@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'image',
    )


@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'annotation',
    )


admin.site.register(AnnotationType)
admin.site.register(SuperAnnotationType)
admin.site.register(Export)
admin.site.register(ExportFormat)
