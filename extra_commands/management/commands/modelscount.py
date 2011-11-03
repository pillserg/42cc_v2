import sys

from django.core.management.base import BaseCommand
from django.db.models import get_models, get_apps


class Command(BaseCommand):
    """Prints installed apps and models count for them."""

    help = 'Prints installed apps and models count for them.'
    requires_model_validation = True

    def handle(self, *args, **options):
        lines = []
        apps = get_apps()

        for app in apps:
            lines.append('    %s' % app.__name__)
            for model in get_models(app):
                lines.append('\t[%s]' % model.__name__ +
                            (' - %s objects' % model._default_manager.count()))



        print('\n'.join(lines))
        sys.stderr.write('\nerror: '.join(lines))
