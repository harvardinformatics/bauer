from django.db import models

# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,
            choices = (('nextseq', 'nextseq'), ('hiseq', 'hiseq')),
            default = 'nextseq')

class Run(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    flowcell = models.CharField(max_length=100, blank = True, null = True)
    lot = models.CharField(max_length=100, blank = True, null = True)
    expiration = models.DateField(blank = True, null = True)
    instrument_id = models.ForeignKey('Instrument', on_delete = models.PROTECT)

class Lane(models.Model):
    number = models.IntegerField()
    run_id = models.ForeignKey('Run', on_delete = models.CASCADE)

class Sample(models.Model):
    name = models.CharField(max_length=100)
    run_id = models.ForeignKey('Run', on_delete = models.PROTECT)
    lane_id = models.ForeignKey('Lane', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    description = models.CharField(max_length=100)
    index1 = models.CharField(max_length=50, blank = True, null = True)
    index2 = models.CharField(max_length=50, blank = True, null = True)

class Read(models.Model):
    number = models.IntegerField()
    run_id = models.ForeignKey('Run', on_delete = models.CASCADE)
    lane_id = models.ForeignKey('Lane', on_delete = models.CASCADE)
    length = models.IntegerField(blank = True, null = True)
    indexed = models.BooleanField(default = False)

class Status(models.Model):
    name = models.CharField(max_length=100,
            choices = (('pending', 'pending'),
        ('processing', 'processing'), ('complete', 'complete'), ('failed',
            'failed')),
            default = 'pending')

class Request(models.Model):
    run_id = models.ForeignKey('Run', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    start_after = models.DateTimeField()
    status_id = models.ForeignKey('Status', on_delete = models.PROTECT)
    requestor = models.CharField(max_length=100, blank = True, null = True)

class AnalysisType(models.Model):
    name = models.CharField(max_length=100,
            choices = (('bcl2fastq', 'bcl2fastq'), ('fastqc', 'fastqc')),
            default = 'bcl2fastq')
    class Meta:
        db_table = 'analysis_type'

class Analysis(models.Model):
    request_id = models.ForeignKey('Request', on_delete = models.PROTECT)
    analysis_type_id = models.ForeignKey('AnalysisType', on_delete =
            models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    cmd = models.CharField(max_length=255)
    start = models.DateTimeField(null = True)
    stop = models.DateTimeField(null = True)
    code = models.IntegerField(null = True)
    pid = models.IntegerField(null = True)
    log = models.CharField(max_length=255, null = True)

class Bcl2fastqSampleAnalysis(models.Model):
    analysis_id = models.ForeignKey('Analysis', on_delete = models.PROTECT)
    sample_id = models.ForeignKey('Sample', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    q30 = models.FloatField()
    cluster = models.IntegerField()
    class Meta:
        db_table = 'bcl2fastq_sample_analysis'
