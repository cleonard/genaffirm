from django import template

register = template.Library()


@register.filter(name="currency")
def currency_display(amount):
    # Currency display given whole dollar amounts: 5000 => $5,000
    return f"${amount:,}"


@register.filter(name="clean_notes")
def clean_notes(notes):
    # Clean up space and replace \n with <br> tags
    lines = notes.strip().splitlines()
    lines = [l.strip() for l in lines]
    return "<br>".join(lines)


@register.filter(name="in_cents")
def in_cents(amount):
    """Stripe takes monetary amounts in cents ($5 == 500 cents)"""
    return int(round(amount * 100))
