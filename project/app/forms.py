from django import forms

from dataclasses import dataclass

class PullRequestForm(forms.Form):
    repository = forms.CharField(
        label='repository',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True            
        }))
    title = forms.CharField(
        label='title',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True            
        }))
    st_pull_request_url = forms.CharField(
        label='st_pull_request_url',
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'oninput': 'updateInputState()'
        }))
    e2e_uat_pull_request_url = forms.CharField(
        label='e2e_uat_pull_request_url',
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True,
            'oninput': 'updateInputState()'
            }))
    main_pull_request_url = forms.CharField(
        label='main_pull_request_url',
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True,
            'oninput': 'updateInputState()'
        }))
    source_branch = forms.CharField(
        label='source_branch',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True
        }))
    target_branch = forms.CharField(
        label='target_branch',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'readonly': True
        }))

    pull_request_id: int

    def get_id_from_pull_request_url(self) -> int:
        """プルリクエストURLからIDを取得する"""
        url = ""
        if not len(self.cleaned_data['main_pull_request_url']) == 0:
            url = self.cleaned_data['main_pull_request_url']
        elif not len(self.cleaned_data['e2e_uat_pull_request_url']) == 0:
            url = self.cleaned_data['e2e_uat_pull_request_url']
        else:
            url = self.cleaned_data['st_pull_request_url']
        trim_url = "https://dev.azure.com/ittimfn/SampleProject/_git/SampleProject/pullrequest/"
        return int(url[len(trim_url):])