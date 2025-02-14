from loguru import logger


def main():
    logger.add('file.log ',
                format= '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
                rotation="3 days",
                backtrace=True,
                diagnose=True)


if __name__ == '__main':
    main()
