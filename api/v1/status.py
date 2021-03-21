"""
Status module to support all the ReST actions for the
STATUS collection
"""

def getStatus():
    """
    This function responds to a request for /api/v1/status
    with a status object
    :return:        status
    """
    statusObject = {
        "Version": "1.0.0"
    }
    return statusObject