# from loguru import logger
# import sys
# config = {
#     "handlers": [
#         {"sink": sys.stdout, "format": "{time} - {message}"},
#     ],
#     "extra": {"user": "someone"}
# }
# logger.configure(**config)

# # For libraries
# logger.disable('my_library')
# logger.info("No matter added sinks, this message is not displayed",
#             name="my_library")
# # logger.enable(None)
# logger.info("This message however is propagated to the sinks",
#             name="my_library")


# def func(a, /, b, *c, d=None):
#     ...


# print(f"{func.__code__.co_varnames = }",
#       f"{func.__code__.co_argcount = }",
#       f"{func.__code__.co_posonlyargcount = }",
#       f"{func.__code__.co_kwonlyargcount = }",
#       f"{func.__code__.co_qualname = }",
#       sep='\n')

# def test(a, b):
#     return True


# str.__le__ = test

# print('a' >= 1)

if a := 1:
    ...

print(a)
