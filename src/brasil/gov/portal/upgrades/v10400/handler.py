# -*- coding:utf-8 -*-

from brasil.gov.portal.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging

logger = logging.getLogger(PROJECTNAME)


def apply_profile(context):
    """Atualiza perfil para versao 10400"""
    profile = 'profile-brasil.gov.portal.upgrades.v10400:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 10400')
