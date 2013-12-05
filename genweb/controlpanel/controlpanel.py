# -*- coding: utf-8 -*-
from z3c.form import button
from zope.component.hooks import getSite
from zope.component import getAdapter
from zope.interface import alsoProvides

from plone.app.registry.browser import controlpanel
# from plone.registry.interfaces import IRecordModifiedEvent
# from plone.app.controlpanel.interfaces import IConfigurationChangedEvent

from Products.statusmessages.interfaces import IStatusMessage
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import _createObjectByType

from genweb.controlpanel.interface import IGenwebControlPanelSettings
from genweb.core import GenwebMessageFactory as _
from genweb.core.interfaces import IProtectedContent
from genweb.packets.interfaces import IpacketDefinition


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

        if data.get('idestudi_master', False):
            portal = getSite()
            if not getattr(portal, 'informacio-general', False):
                info_general = _createObjectByType('packet', portal, 'informacio-general', title=_(u"General information"))
                adapter = getAdapter(info_general, IpacketDefinition, 'fitxa_master')
                field_values = {u'codi_master': data['idestudi_master']}
                adapter.packet_fields = field_values
                adapter.packet_type = 'fitxa_master'
                info_general.exclude_from_nav = True
                alsoProvides(info_general, IProtectedContent)

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
