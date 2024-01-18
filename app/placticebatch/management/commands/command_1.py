from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "コマンドの説明"

    def add_arguments(self, parser):
        parser.add_argument("--name", nargs="1", default="", type=str)

    def handle(self, *args, **options):
        print(f"渡された引数は{options['name']}")
