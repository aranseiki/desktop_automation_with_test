def logging_msg(message, level, filename=None, filemode=None, encoding=None, format=None, handlers=None):
    # import logging resources
    from logging import basicConfig, debug, info, warning, error, critical, DEBUG, INFO, WARNING, ERROR, CRITICAL
    
    # define level
    level = level.upper()

    # define basic config
    basicConfig(
        level = level,
        filename = filename,
        filemode = filemode,
        encoding = encoding,
        format = format,
        handlers = handlers
    )

    # run logging command
    if level == 'DEBUG':
        debug(message)
    elif level == 'INFO':
        info(message)
    elif level == 'WARNING':
        warning(message)
    elif level == 'ERROR':
        error(message)
    elif level == 'CRITICAL':
        critical(message)
    else:
        return 'Level parameter invalid. Please, Inform this correctly.'

    # return message and level
    return (message, level)