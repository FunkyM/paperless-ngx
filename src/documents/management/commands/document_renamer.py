import logging

from django.core.management.base import BaseCommand
from documents.tasks import update_all_documents

class Command(BaseCommand):

    help = """
        This will rename all documents to match the latest filename format.
    """.replace(
        "    ",
        "",
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-progress-bar",
            default=False,
            action="store_true",
            help="If set, the progress bar will not be shown",
        )

    def handle(self, *args, **options):

        logging.getLogger().handlers[0].level = logging.ERROR

        update_all_documents(options["no_progress_bar"])
