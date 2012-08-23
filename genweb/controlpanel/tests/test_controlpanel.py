# -*- coding: utf-8 -*-
import unittest2 as unittest

from zope.component import getMultiAdapter
from zope.component import queryUtility

from plone.registry import Registry
from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName

from plone.app.testing import TEST_USER_ID, setRoles

from genweb.controlpanel.interface import IGenwebControlPanelSettings
from genweb.controlpanel.testing import GENWEBCONTROLPANEL_INTEGRATION_TESTING


class RegistryTest(unittest.TestCase):

    layer = GENWEBCONTROLPANEL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.registry = Registry()
        self.registry.registerInterface(IGenwebControlPanelSettings)

    def test_registry_registered(self):
        registry = queryUtility(IRegistry)
        self.assertTrue(registry.forInterface(IGenwebControlPanelSettings))

    def test_discussion_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="genweb-controlpanel")
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_discussion_in_controlpanel(self):
        # Check if discussion is in the control panel
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.assertTrue('genweb' in [a.getAction(self)['id']
                            for a in self.controlpanel.listActions()])

    def test_unicode_values(self):
        registry = queryUtility(IRegistry)
        genweb_settings = registry.forInterface(IGenwebControlPanelSettings)
        genweb_settings.html_title_ca = u"àéçÀÉ"
        self.assertEqual(genweb_settings.html_title_ca, u"àéçÀÉ")
