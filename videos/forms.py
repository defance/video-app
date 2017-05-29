# coding=utf-8

from __future__ import unicode_literals

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


class NewVideoForm(forms.Form):
    id = forms.CharField(label='id')
    video = forms.FileField(label='Видео файл')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    helper.layout = Layout(
        Field('id'),
        Field('video'),
        FormActions(
            Submit('save_changes', 'Загрузить видео', css_class="btn-primary"),
        )
    )

    def video_upload(self):
        print "video upload"
