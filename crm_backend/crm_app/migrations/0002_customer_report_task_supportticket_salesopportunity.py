# Generated by Django 4.2.6 on 2023-10-17 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("job_title", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("interactions", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("sales_funnel", "Sales Funnel"),
                            ("customer_interaction", "Customer Interaction"),
                            ("monthly_sales", "Monthly Sales"),
                        ],
                        max_length=50,
                    ),
                ),
                ("data", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("due_date", models.DateTimeField()),
                ("reminder", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SupportTicket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("issue_description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("in_progress", "In Progress"),
                            ("closed", "Closed"),
                        ],
                        max_length=50,
                    ),
                ),
                ("response", models.TextField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_app.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SalesOpportunity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "expected_revenue",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "current_stage",
                    models.CharField(
                        choices=[
                            ("initial_contact", "Initial Contact"),
                            ("proposal", "Proposal/Quote"),
                            ("negotiation", "Negotiation/Review"),
                            ("closed", "Closed"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_app.customer",
                    ),
                ),
            ],
        ),
    ]
