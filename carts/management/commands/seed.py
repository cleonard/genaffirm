import random
import re

from django.core.management.base import BaseCommand

from carts.models import Category, Product

RE_HEADLINE = re.compile(r"^# *")

data = """
# Pain Treatments
Tissue Transplant Injection	4500
Softwave Package (8)	1600
TTI Booster	600
General Wellness IV	5000
# Hair Restoration
Protocol 1 (3 Treatments)	3750
Protocol 2 (3 Treatments)	15000
Protocol 3 (3 Treatments)	30000
# Aesthetics
Microneedling Treatment (3 treatments)	2100
NeuroToxin	600
""".strip().splitlines()


class Command(BaseCommand):
    help = "Seed categories and products if they are empty"

    def handle(self, *args, **options):
        category_count = Category.objects.count()
        product_count = Product.objects.count()

        if category_count or product_count:
            self.stdout.write(
                self.style.ERROR(
                    "Aborting: categories and/or products are already populated.",
                )
            )
            return None

        category = None
        category_sort = 1
        for line in data:
            if line.startswith("# "):
                category_name = RE_HEADLINE.sub("", line).strip()
                category = Category.objects.create(
                    name=category_name,
                    sort=category_sort,
                )
                category_sort += 1
            else:
                name, amount = line.split("\t")
                Product.objects.create(
                    name=name.strip(),
                    amount=int(amount),
                    category=category,
                )
        self.stdout.write(self.style.SUCCESS("Done"))
