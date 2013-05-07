# -*- coding: utf-8 -*-
from z3c.form import button

from plone.app.registry.browser import controlpanel
# from plone.registry.interfaces import IRecordModifiedEvent
# from plone.app.controlpanel.interfaces import IConfigurationChangedEvent

from Products.statusmessages.interfaces import IStatusMessage
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from genweb.controlpanel.interface import IGenwebControlPanelSettings
from genweb.core import GenwebMessageFactory as _


class GenwebControlPanelSettingsForm(controlpanel.RegistryEditForm):
    """ Genweb settings form """

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
    """ Genweb settings control panel """
    form = GenwebControlPanelSettingsForm
    # index = ViewPageTemplateFile('controlpanel.pt')
