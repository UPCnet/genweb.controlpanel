# -*- coding: utf-8 -*-
from plone import api
from five import grok
from zope import schema
from zope.interface import Interface
from z3c.form import button
from plone.supermodel import model
from zope.component import getUtilitiesFor
from plone.app.registry.browser import controlpanel
from zope.schema.interfaces import IContextSourceBinder
from souper.interfaces import ICatalogFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import directlyProvides

from Products.statusmessages.interfaces import IStatusMessage

from genweb.core import GenwebMessageFactory as _

import pkg_resources

try:
    pkg_resources.get_distribution('genweb.upc')
except pkg_resources.DistributionNotFound:
    IAMGENWEBUPC = False
else:
    IAMGENWEBUPC = True


class RegisteredExtendersVocabulary(object):

    def __call__(self, context):
        terms = []
        extenders = [a[0] for a in getUtilitiesFor(ICatalogFactory) if a[0].startswith('user_properties') and a[0] != 'user_properties']
        for extender in extenders:
            terms.append(SimpleVocabulary.createTerm(extender, str(extender), extender))
        return SimpleVocabulary(terms)

RegisteredExtendersVocabularyFactory = RegisteredExtendersVocabulary()


class IGenwebCoreControlPanelSettings(Interface):
    """ Global Genweb settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    user_properties_extender = schema.Choice(
        title=_(u'User properties extender'),
        vocabulary=u'genweb.controlpanel.core.user_extenders',
        required=False,
        default=u''
    )


class GenwebCoreControlPanelSettingsForm(controlpanel.RegistryEditForm):
    """ Genweb settings form """

    schema = IGenwebCoreControlPanelSettings
    id = "GenwebCoreControlPanelSettingsForm"
    label = _(u"Genweb Core settings")
    description = _(u"help_genweb_core_settings_editform",
                    default=u"Configuració de Genweb Core")

    def updateFields(self):
        super(GenwebCoreControlPanelSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(GenwebCoreControlPanelSettingsForm, self).updateWidgets()

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        self.applyChanges(data)

        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"), "info")
        self.context.REQUEST.RESPONSE.redirect("@@genweb-controlpanel")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"), "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))


class GenwebCoreControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Genweb Core settings control panel """
    form = GenwebCoreControlPanelSettingsForm
