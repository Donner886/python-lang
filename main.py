import functools




def suppress_errors(func):
    '''
    Automatically silence any errors that occur within a function
    :param func:
    :return:
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('訪問控制開始')
            return func(*args, **kwargs)
            print('訪問控制結束')
        except Exception:
            pass
    return wrapper



import datetime
#%%
@suppress_errors
def log_error(message, log_file='errors.log'):
    """
    Log an error to a file:
    :param message:
    :param log_file:
    :return:
    """
    log = open(log_file, 'w')
    log.write('%s\t%s\n' % (datetime.datetime.now(), message))

if __name__ == '__main__':
    suppress_errors('trial on logging errors function')
