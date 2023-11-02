from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verification_code = models.CharField(max_length=6, blank=True, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    interactions = models.TextField(blank=True)


class SalesOpportunity(models.Model):
    OPPORTUNITY_STAGES = [
        ('initial_contact', 'Initial Contact'),
        ('proposal', 'Proposal/Quote'),
        ('negotiation', 'Negotiation/Review'),
        ('closed', 'Closed'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expected_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    current_stage = models.CharField(max_length=50, choices=OPPORTUNITY_STAGES)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    reminder = models.DateTimeField(blank=True, null=True)


class Report(models.Model):
    REPORT_TYPES = [
        ('sales_funnel', 'Sales Funnel'),
        ('customer_interaction', 'Customer Interaction'),
        ('monthly_sales', 'Monthly Sales'),
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    data = models.TextField()  # You can store the data in JSON format or link to another model for detailed data


class SupportTicket(models.Model):
    TICKET_STATUS = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue_description = models.TextField()
    status = models.CharField(max_length=50, choices=TICKET_STATUS)
    response = models.TextField(blank=True, null=True)
