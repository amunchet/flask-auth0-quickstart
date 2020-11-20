# Permissions scope names
from common import auth
import functools

PERM_READ = "read:XXXX"
PERM_WRITE = "write:XXXX"
PERM_ADMIN = "reports:XXXX"


requires_auth_read = functools.partial(auth._requires_auth, permission=PERM_READ)
requires_auth_write = functools.partial(auth._requires_auth, permission=PERM_WRITE)
requires_auth_reports = functools.partial(auth._requires_auth, permission=PERM_ADMIN