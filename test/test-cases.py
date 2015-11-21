import unittest
from subprocess import Popen, PIPE

def run(args):
  command = ['coverage', 'run', '--branch', '-a', '../make-prefetch.py'] + args
  process = Popen(command, stdout=PIPE, stderr=PIPE)
  (stdout, stderr) = process.communicate();
  return (process.returncode, stdout, stderr)

class TestHelp(unittest.TestCase):

  def test_help_short(self):
    (exitcode, stdout, stderr) = run(['-h'])
    self.assertEqual(exitcode, 0)
    self.assertTrue('Create a prefetch statement' in stdout)

  def test_help_long(self):
    (exitcode, stdout, stderr) = run(['--help'])
    self.assertEqual(exitcode, 0)
    self.assertTrue('Create a prefetch statement' in stdout)

class TestURL(unittest.TestCase):

  def test_url(self):
    (exitcode, stdout, stderr) = run(['http://localhost:36465/hodor.txt'])

    expected = (
      'prefetch '
      'hodor.txt '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://localhost:36465/hodor.txt '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_url_name(self):
    (exitcode, stdout, stderr) = run(['--name', 'bran.txt',
                                      'http://localhost:36465/hodor.txt'])

    expected = (
      'prefetch '
      'bran.txt '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://localhost:36465/hodor.txt '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_url_no_name(self):
    (exitcode, stdout, stderr) = run(['http://localhost:36465/'])

    expected = (
      'prefetch '
      'REPLACEME '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://localhost:36465/ '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

class TestFile(unittest.TestCase):

  def test_file(self):
    (exitcode, stdout, stderr) = run(['hodor.txt'])

    expected = (
      'prefetch '
      'hodor.txt '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://REPLACEME '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_sha1(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-a', 'sha1'])

    expected = (
      'prefetch '
      'hodor.txt '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://REPLACEME'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_sha256(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-a', 'sha256'])

    expected = (
      'prefetch '
      'hodor.txt '
      'size:5 '
      'http://REPLACEME '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_url(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-u', 'http://example.com'])

    expected = (
      'prefetch '
      'hodor.txt '
      'sha1:c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size:5 '
      'http://example.com '
      'sha256:aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_value_sha1(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-o', 'value', '-a', 'sha1'])

    expected = 'c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687'

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_value_sha256(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-o', 'value', '-a',
                                      'sha256'])

    expected = (
      'aa116aa7b00b3006a1cf72219634cb1edbfad6abb1708c2e01b0409800f958b5'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_value_error(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-o', 'value'])

    self.assertEqual(exitcode, 2)
    self.assertEqual('You must specify a hash algorithm to use', stderr.strip())

  def test_file_value_davis(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-o', 'davis'])

    expected = (
      'begin prefetch block\n'
      'add prefetch item '
      'name=hodor.txt '
      'sha1=c6447b82fbb4b8e7dbcf2d28a4d7372f5dc32687 '
      'size=5 '
      'url=http://REPLACEME\n'
      'collect prefetch items\n'
      'end prefetch block'
    )

    self.assertEqual(exitcode, 0)
    self.assertEqual(expected, stdout.strip())

  def test_file_value_davis_error(self):
    (exitcode, stdout, stderr) = run(['hodor.txt', '-o', 'davis', '-a',
                                      'sha256'])

    expected = 'Algorithm sha256 is not supported in davis downloads'

    self.assertEqual(exitcode, 2)
    self.assertEqual(expected, stderr.strip())

if __name__ == '__main__':
  unittest.main()
