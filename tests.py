import unittest

import msglite


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_unicode_message(self):
        msg = msglite.Message("example-msg-files/unicode.msg")
        # msg.dump()
        # msg.debug()
        # print(msg.attachments)
        self.assertEqual(msg.subject, u"Test for TIF files")
        self.assertEqual(
            msg.body,
            u"This is a test email to experiment with the MS Outlook MSG "
            u"Extractor\r\n\r\n\r\n-- \r\n\r\n\r\nKind regards"
            u"\r\n\r\n\r\n\r\n\r\nBrian Zhou\r\n\r\n",
        )
        self.assertEqual(msg.date, "Mon, 18 Nov 2013 08:26:24 +0000")
        self.assertEqual(msg.sender, "Brian Zhou <brizhou@gmail.com>")
        self.assertEqual(msg.to, ["brianzhou@me.com"])
        self.assertEqual(msg.cc, ["Brian Zhou <brizhou@gmail.com>"])
        self.assertEqual(len(msg.attachments), 2)

    def test_norse_message(self):
        msg = msglite.Message("example-msg-files/norse.msg")
        self.assertIn("Byggemøtereferat", msg.subject)
        self.assertIn("byggemøtereferat", msg.body)
        self.assertIn("byggemøtereferat", msg.htmlBody)

    def test_sample_message(self):
        msg = msglite.Message("example-msg-files/sample.msg")
        self.assertEqual(msg.to, ["sales@bitdaddys.com"])

    def test_rom_message(self):
        msg = msglite.Message("example-msg-files/rom.msg")
        self.assertIn("așteptăm", msg.body)


unittest.main(verbosity=2)
