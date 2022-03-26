import sys
import traceback

from base.settings import ERROR_LOGGER


def handle_exceptions():
    ex_type, ex_value, ex_traceback = sys.exc_info()
    trace_back = traceback.extract_tb(ex_traceback)

    log = "Exception type : %s" % ex_type.__name__
    log2 = "Exception message : %s" % ex_value
    # Format stacktrace
    stack_trace = list()

    log3 = ""
    for trace in trace_back:
        errorContent = "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3])
        stack_trace.append(errorContent)
        log3 += f"Stack trace: {errorContent}\n"

    ERROR_LOGGER.error(log)
    ERROR_LOGGER.error(log2)
    ERROR_LOGGER.error(log3)
