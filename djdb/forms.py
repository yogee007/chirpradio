###
### Copyright 2009 The Chicago Independent Radio Project
### All Rights Reserved.
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###     http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
###

"""Forms for DJ Database."""

from django import forms
from djdb import models
from common.autoretry import AutoRetry

ALBUM_CATEGORY_CHOICES = [["", ""]]
ALBUM_CATEGORY_CHOICES += zip(models.ALBUM_CATEGORIES,
                              [category.replace('_', ' ').capitalize() for category in models.ALBUM_CATEGORIES])

class PartialAlbumForm(forms.Form):
    label = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'size': 40}))
    year = forms.IntegerField(required=False,
                              widget=forms.TextInput(attrs={'size': 4, 'maxlength': 4}))

class ListReviewsForm(forms.Form):
    author = forms.CharField(required=False)
    author_key = forms.CharField(required=False, widget=forms.HiddenInput)
    category = forms.ChoiceField(required=False, choices=ALBUM_CATEGORY_CHOICES)