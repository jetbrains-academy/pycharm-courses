import logging
import re

class SanitizeSSNFilter(logging.Filter):
    def filter(self, record):
        def replace_ssn(value):
            return re.sub('\d\d\d-\d\d-\d\d\d\d', 'XXX-XX-XXXX', value)

        record.msg = replace_ssn(record.msg)
        if record.args:
            newargs = [replace_ssn(arg) if isinstance(arg, str)
                       else arg for arg in record.args]
            record.args = tuple(newargs)

        return insert the appropriate return value

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    sanitize_filter = SanitizeSSNFilter()
    root = logging.getLogger()
    add the filter object to the root logger

    root.debug('Nothing filtered here; user_id=%s', '100')
    root.debug('Log message containing a SSN=000-01-1000')
    root.warn('Log message containing a SSN=%s', '000-01-1001')
    root.debug('Log message containing a SSN=%s' % '000-01-1100')
    root.info('Log event: user_id=%s, SSN=%s, status=%d, result=%s', '100', '000-01-1100', 2, True)
