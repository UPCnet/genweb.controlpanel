# -*- coding: utf-8 -*-

from Acquisition import aq_base, aq_inner

from Products.CMFCore.utils import getToolByName

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.statusmessages.interfaces import IStatusMessage

from plone.app.controlpanel.interfaces import IConfigurationChangedEvent

from plone.app.registry.browser import controlpanel

from plone.registry.interfaces import IRegistry
from plone.registry.interfaces import IRecordModifiedEvent

from zope.component.hooks import getSite
from zope.component import getMultiAdapter, queryUtility

from z3c.form import button
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget

from genweb.controlpanel.interface import IGenwebControlPanelSettings
from genweb.core import GenwebMessageFactory as _


class GenwebControlPanelSettingsForm(controlpanel.RegistryEditForm):
    """ Genweb settings form. """

    schema = IGenwebControlPanelSettings
    id = "GenwebControlPanelSettingsForm"
    label = _(u"Genweb UPC settings")
    description = _(u"help_genweb_settings_editform",
                    default=u"Configuració de Genweb UPC ...")

    def updateFields(self):
        super(GenwebControlPanelSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(GenwebControlPanelSettingsForm, self).updateWidgets()

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect("@@genweb-controlpanel")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"),
                                                      "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))


class GenwebControlPanel(controlpanel.ControlPanelFormWrapper):
    """Discussion settings control panel.
    """
    form = GenwebControlPanelSettingsForm
    # index = ViewPageTemplateFile('controlpanel.pt')
