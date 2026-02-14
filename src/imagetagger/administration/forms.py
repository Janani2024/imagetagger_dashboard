from django import forms

from imagetagger.annotations.models import AnnotationType, SuperAnnotationType


class SuperAnnotationTypeCreationForm(forms.ModelForm):
    class Meta:
        model = SuperAnnotationType
        fields = [
            'name',
            'active',
        ]


class SuperAnnotationTypeEditForm(forms.ModelForm):
    class Meta:
        model = SuperAnnotationType
        fields = [
            'name',
            'active',
        ]


class AnnotationTypeCreationForm(forms.ModelForm):
    class Meta:
        model = AnnotationType
        fields = [
            'name',
            'active',
            'node_count',
            'vector_type',
            'enable_concealed',
            'enable_blurred',
            'super_annotation_type',
        ]


class AnnotationTypeEditForm(forms.ModelForm):
    class Meta:
        model = AnnotationType
        fields = [
            'name',
            'active',
            'enable_concealed',
            'enable_blurred',
            'super_annotation_type',
        ]
