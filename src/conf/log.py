import logging

log = logging.Logger(
    name="PITSBURG"
)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
streamHandler.setFormatter(logging.Formatter("%(levelname)s\t%(asctime)s\t%(name)s\t%(message)s", datefmt="%Y-%m-%dT%H:%M:%S"))


log.addHandler(streamHandler)
