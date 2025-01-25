from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from compressor.contrib.jinja2ext import CompressorExtension


def environment(**options):
    env = Environment(**options)

    # Add CompressorExtension
    env.add_extension(CompressorExtension)

    # Basic Django Functions
    env.globals.update({
        'static': static,
        'url': reverse,
    })

    # Add custom filters
    env.filters.update({
    })

    # Add custom tests
    env.tests.update({
    })

    return env