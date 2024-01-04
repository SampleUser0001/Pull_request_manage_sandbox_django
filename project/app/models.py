from django.db import models

from .forms import PullRequestForm

class PullRequestModel(models.Model):
    '''PR情報を管理するモデル'''
    repository = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    st_pull_request_url = models.CharField(max_length=1000)
    e2e_uat_pull_request_url = models.CharField(max_length=1000)
    main_pull_request_url = models.CharField(max_length=1000)
    
    source_branch = models.CharField(max_length=255)
    target_branch = models.CharField(max_length=255)
    
    pull_request_id = models.IntegerField()

    def set_Form(self, form: PullRequestForm):
        '''FormからModelに値を設定する'''
        self.repository = form.cleaned_data['repository']
        self.title = form.cleaned_data['title']
        self.st_pull_request_url = form.cleaned_data['st_pull_request_url']
        self.e2e_uat_pull_request_url = form.cleaned_data['e2e_uat_pull_request_url']
        self.main_pull_request_url = form.cleaned_data['main_pull_request_url']
        self.source_branch = form.cleaned_data['source_branch']
        self.target_branch = form.cleaned_data['target_branch']
        try:
            self.pull_request_id = form.get_id_from_pull_request_url()
        except (KeyError, ValueError):
            self.pull_request_id = 0
        

    def __str__(self):
        '''Adminページに表示する文言を設定する'''
        return self.message
