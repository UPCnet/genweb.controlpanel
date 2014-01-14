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
from Products.CMFCore.utils import getToolByName

from genweb.controlpanel.interface import IGenwebControlPanelSettings
from genweb.core import GenwebMessageFactory as _
from genweb.core.interfaces import IProtectedContent

import pkg_resources

try:
    pkg_resources.get_distribution('genweb.upc')
except pkg_resources.DistributionNotFound:
    IAMGENWEBUPC = False
else:
    IAMGENWEBUPC = True
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

    def setLanguageAndLink(self,items):
        canonical,canonical_lang = items[0]
        for item,language in items:
            item.setLanguage(language)
            if item!=canonical and canonical_lang not in item.getTranslations().keys():
                item.addTranslationReference(canonical)

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)

        if IAMGENWEBUPC:
            
            if data.get('idestudi_master', False):
                portal = getSite()
                if getattr(portal, 'informacio-general', False): 
                # Si fiquem un altre id, i ja existeix l'esborrem i el tornem a crear amb el nou id
                    portal.manage_delObjects('informacio-general')
                    portal.manage_delObjects('informacion-general')
                    portal.manage_delObjects('general-information')

                if not getattr(portal, 'informacio-general', False): 
                # Com que ja no existeix, el creem

                    lt = getToolByName(portal, 'portal_languages')
                    currentLang=lt.getPreferredLanguage()

                    info_ca = _createObjectByType('packet', portal, 'informacio-general', title=u"Informació general del Màster")
                    info_es = _createObjectByType('packet', portal, 'informacion-general', title=u"Información general del Máster")
                    info_en = _createObjectByType('packet', portal, 'general-information', title=u"General information of the Degree Studies")
                    self.setLanguageAndLink([(info_ca,'ca'),(info_es,'es'),(info_en,'en')])

                    adapter = getAdapter(info_ca, IpacketDefinition, 'fitxa_master')
                    field_values = {u'codi_master': data['idestudi_master']}
                    adapter.packet_fields = field_values
                    adapter.packet_type = 'fitxa_master'
                    info_ca.exclude_from_nav = True
                    alsoProvides(info_ca, IProtectedContent)

                    adapter = getAdapter(info_es, IpacketDefinition, 'fitxa_master')
                    field_values = {u'codi_master': data['idestudi_master']}
                    adapter.packet_fields = field_values
                    adapter.packet_type = 'fitxa_master'
                    info_es.exclude_from_nav = True
                    alsoProvides(info_es, IProtectedContent)

                    adapter = getAdapter(info_en, IpacketDefinition, 'fitxa_master')
                    field_values = {u'codi_master': data['idestudi_master']}
                    adapter.packet_fields = field_values
                    adapter.packet_type = 'fitxa_master'
                    info_en.exclude_from_nav = True
                    alsoProvides(info_en, IProtectedContent)

                    IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"), "info")
                    self.context.REQUEST.RESPONSE.redirect("@@genweb-controlpanel")


    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"), "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))


class GenwebControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Genweb settings control panel """
    form = GenwebControlPanelSettingsForm
    # index = ViewPageTemplateFile('controlpanel.pt')
