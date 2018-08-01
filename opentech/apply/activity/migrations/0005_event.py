# Generated by Django 2.0.2 on 2018-07-30 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_update_on_delete_django2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('UPDATE_LEAD', 'Update Lead'), ('NEW_SUBMISSION', 'New Submission'), ('TRANSITION', 'Transition'), ('DETERMINATION_OUTCOME', 'Determination Outcome'), ('INVITED_TO_PROPOSAL', 'Invited To Proposal'), ('REVIEWERS_UPDATED', 'Reviewers Updated'), ('READY_FOR_REVIEW', 'Ready For Review'), ('NEW_REVIEW', 'New Review'), ('COMMENT', 'Comment'), ('PROPOSAL_SUBMITTED', 'Proposal Submitted')], max_length=50)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.ApplicationSubmission', related_name='+')),
            ],
        ),
    ]
