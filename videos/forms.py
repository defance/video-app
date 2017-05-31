# coding=utf-8

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

from .models import Video


class NewVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('id', 'video', 'category')

    def __init__(self, *args, **kwargs):
        self.random_id = kwargs.pop('random_id')
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal upload-video'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Field('id', placeholder=self.random_id),
            Field('category'),
            Field('video', accept='.mp4, .avi'),
            FormActions(
                Submit(
                    'save_changes', _('Upload'), css_class="btn-primary",
                    data_msg_uploading=_('Uploading...')
                ),
            )
        )
        super(NewVideoForm, self).__init__(*args, **kwargs)
