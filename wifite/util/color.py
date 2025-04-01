#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Color(object):
    ''' Helper object for easily printing colored text to the terminal. '''

    
    colors = {
        'W': '\033[0m',   # White (reset/normal)
        'R': '\033[91m',  # Bright Red
        'G': '\033[92m',  # Bright Green
        'O': '\033[93m',  # Bright Orange/Yellow
        'B': '\033[94m',  # Bright Blue
        'P': '\033[95m',  # Bright Purple/Magenta
        'C': '\033[96m',  # Bright Cyan
        'GR': '\033[90m', # Bright Gray
        'D': '\033[2m',   # Dimmed/Gray
        'Y': '\033[33m',  # Dark Yellow
        'M': '\033[35m',  # Magenta
    }

    # Custom symbols with updated colors
    replacements = {
        '{+}': ' {W}{D}[{W}{G}+{W}{D}]{W}',
        '{!}': ' {O}[{R}!{O}]{W}',
        '{?}': ' {W}[{C}?{W}]',
        '{*}': ' {W}[{B}*{W}]',
        '{-}': ' {W}[{M}-{W}]',
    }

    last_sameline_length = 0

    @staticmethod
    def p(text):
        '''
        Prints text using colored format on the same line.
        Example:
            Color.p('{R}This text is red. {W} This text is white')
        '''
        sys.stdout.write(Color.s(text))
        sys.stdout.flush()
        if '\r' in text:
            text = text[text.rfind('\r') + 1:]
            Color.last_sameline_length = len(text)
        else:
            Color.last_sameline_length += len(text)

    @staticmethod
    def pl(text):
        '''Prints text using colored format with trailing newline.'''
        Color.p('%s\n' % text)
        Color.last_sameline_length = 0

    @staticmethod
    def pe(text):
        '''Prints text using colored format to STDERR with a newline.'''
        sys.stderr.write(Color.s('%s\n' % text))
        Color.last_sameline_length = 0

    @staticmethod
    def s(text):
        '''Returns colored string'''
        output = text
        for (key, value) in Color.replacements.items():
            output = output.replace(key, value)
        for (key, value) in Color.colors.items():
            output = output.replace('{%s}' % key, value)
        return output

    @staticmethod
    def clear_line():
        spaces = ' ' * Color.last_sameline_length
        sys.stdout.write('\r%s\r' % spaces)
        sys.stdout.flush()
        Color.last_sameline_length = 0

    @staticmethod
    def clear_entire_line():
        import os
        (rows, columns) = os.popen('stty size', 'r').read().split()
        Color.p('\r' + (' ' * int(columns)) + '\r')

    @staticmethod
    def pattack(attack_type, target, attack_name, progress):
        '''
        Prints a one-liner for an attack.
        Includes attack type (WEP/WPA), target ESSID & power, attack type, and progress.
        Example:
        Router2G (23db) WEP replay attack: 102 IVs
        '''
        essid = '{C}%s{W}' % target.essid if target.essid_known else '{O}unknown{W}'
        Color.p('\r{+} {G}%s{W} ({B}%sdb{W}) {M}%s {C}%s{W}: %s ' % (
            essid, target.power, attack_type, attack_name, progress))

    @staticmethod
    def pexception(exception):
        '''Prints an exception. Includes stack trace if necessary.'''
        Color.pl('\n{!} {R}Error: {O}%s' % str(exception))

        # Don't dump trace for the "no targets found" case.
        if 'No targets found' in str(exception):
            return

        from ..config import Configuration
        if Configuration.verbose > 0 or Configuration.print_stack_traces:
            Color.pl('\n{!} {Y}Full stack trace below')
            from traceback import format_exc
            Color.p('\n{!}    ')
            err = format_exc().strip()
            err = err.replace('\n', '\n{!} {C}   ')
            err = err.replace('  File', '{W}File')
            err = err.replace('  Exception: ', '{R}Exception: {O}')
            Color.pl(err)


if __name__ == '__main__':
    Color.pl('{R}Testing {G}Green {C}Cyan {P}Purple {Y}Yellow {B}Blue {W}Done')
    print(Color.s('{C}Testing {P}String {M}With Magenta {W}'))
    Color.pl('{+} Good line')
    Color.pl('{!} Danger')
    Color.pl('{*} Info Message')
    Color.pl('{-} Warning Message')
