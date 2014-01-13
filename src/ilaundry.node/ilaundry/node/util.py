# -*- coding: utf-8 -*-
# (c) 2014 Andreas Motl, Elmyra UG <andreas.motl@elmyra.de>
import os
import sys

def tts_say(message, language='de'):

    # FIXME: add queue here
    print "say:", message

    # Google Translate TTS
    # FIXME: urlescape "message"
    tts_url = 'http://translate.google.com/translate_tts?tl={language}&q={message}'.format(language=language, message=message)
    more_args = ''
    if sys.platform.startswith('linux'):
        # TODO: dynamic configuration of output device
        more_args += '-ao alsa:device=hw=1.0'

    command = "mplayer -really-quiet -noconsolecontrols {more_args} '{resource}'".format(more_args=more_args, resource=tts_url)
    # FIXME: don't do this synchronously
    # FIXME: show errors (stdout/stderr) if command fails
    os.system(command)
