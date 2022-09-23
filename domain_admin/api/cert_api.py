# -*- coding: utf-8 -*-
from flask import request

from domain_admin.utils.cert_util import get_cert_info
from domain_admin.utils.flask_ext.app_exception import AppException


def get_cert_information():
    """
    获取域名证书信息
    :return:
    """
    if request.method == 'GET':
        domain = request.args.get('domain')
    else:
        domain = request.json.get('domain')

    if not domain:
        raise AppException('参数缺失：domain')

    return get_cert_info(domain)