from Products.CMFCore.utils import getToolByName

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class GenwebControlPanel(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import genweb.controlpanel
        xmlconfig.file('configure.zcml',
                       genweb.controlpanel,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'genweb.controlpanel:default')

GENWEBCONTROLPANEL_FIXTURE = GenwebControlPanel()
GENWEBCONTROLPANEL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEBCONTROLPANEL_FIXTURE,),
    name="GenwebControlPanel:Integration")
GENWEBCONTROLPANEL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEBCONTROLPANEL_FIXTURE,),
    name="GenwebControlPanel:Functional")
