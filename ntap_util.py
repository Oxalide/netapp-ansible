#!/usr/bin/python

from ansible.module_utils.basic import *
import ssl
from NaServer import *

def ntap_argument_spec():
    return dict(
        cluster=dict(required=True),
        user_name=dict(required=True),
        password=dict(required=True),
        val_certs=dict(type='bool', default=True),
    )

def invoke_elem_no_verify():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
        
    except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
    else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def connect_to_api(module):
    cluster = module.params['cluster']
    user_name = module.params['user_name']
    password = module.params['password']
    val_certs = module.params['val_certs']

    if not val_certs:
        invoke_elem_no_verify()

    connection = NaServer(cluster, 1 , 0)
    connection.set_server_type("FILER")
    connection.set_transport_type("HTTPS")
    connection.set_port(443)
    connection.set_style("LOGIN")
    connection.set_admin_user(user_name, password)