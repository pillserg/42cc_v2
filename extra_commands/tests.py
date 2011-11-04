import datetime
import os
import re
import subprocess

from tddspry.django import TestCase

from django.conf import settings


class CommandTest(TestCase):
    def test_mycommand_failure(self):
        MIN_NUM_OF_MODELS = 9
        shell_script_path = os.path.join(settings.PROJECT_PATH,
                                         "count_models.sh")

        filename = datetime.datetime.now().date().strftime('%Y-%m-%d') + '.dat'
        full_filename = os.path.join(settings.PROJECT_PATH, filename)

        with open('/dev/null', 'w') as devnull:
            subprocess.call([shell_script_path, ], shell=True, stdout=devnull)
        with open(full_filename) as f:
            num_models_in_output = len(re.findall('\[.+\]', f.read()))
        try:
            os.remove(full_filename)
        except OSError:
            pass

        self.failUnless(num_models_in_output >= MIN_NUM_OF_MODELS,
                         'models list are too small - %s' %
                         num_models_in_output)
