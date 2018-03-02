# -*- coding: utf-8 -*-
from plone import api
from z3c.form import button
from zope.component.hooks import getSite
from zope.component import getAdapter
from zope.interface import alsoProvides

from plone.app.registry.browser import controlpanel
from plone.dexterity.utils import createContentInContainer

from Products.statusmessages.interfaces import IStatusMessage
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
    from plone.app.multilingual.interfaces import ITranslationManager


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

    def link_translations(self, items):
        """
            Links the translations with the declared items with the form:
            [(obj1, lang1), (obj2, lang2), ...] assuming that the first element
            is the 'canonical' (in PAM there is no such thing).
        """
        # Grab the first item object and get its canonical handler
        canonical = ITranslationManager(items[0][0])

        for obj, language in items:
            if not canonical.has_translation(language):
                canonical.register_translation(language, obj)

    def create_content(self, container, portal_type, id, **kwargs):
        if not getattr(container, id, False):
            obj = createContentInContainer(container, portal_type, checkConstraints=False, **kwargs)
            self.publish_content(obj)
        return getattr(container, id)

    def publish_content(self, context):
        """ Make the content visible either in both possible genweb.simple and
            genweb.review workflows.
        """
        pw = getToolByName(context, "portal_workflow")
        object_workflow = pw.getWorkflowsFor(context)[0].id
        object_status = pw.getStatusOf(object_workflow, context)
        if object_status:
            api.content.transition(obj=context, transition={'genweb_simple': 'publish', 'genweb_review': 'publicaalaintranet'}[object_workflow])

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        create_packet = False
        if data.get('create_packet'):
            create_packet = True
            data['create_packet'] = False

        try:
            self.applyChanges(data)
        except:
            from zope.component import getUtility
            from plone.registry.interfaces import IRegistry
            registry = getUtility(IRegistry)
            rec = registry.records
            keys = [a for a in rec.keys()]
            for k in keys:
                try:
                    rec[k]
                except:
                    if k == 'genweb.controlpanel.interface.IGenwebControlPanelSettings.contact_emails_table':
                        old_values = data['contact_emails_table']
                        from plone.registry import Record, field
                        from genweb.core import GenwebMessageFactory as _
                        from collective.z3cform.datagridfield.registry import DictRow
                        from genweb.controlpanel.interface import ITableEmailContact
                        registry.records[k] = Record(field.List(title=_(u'Contact emails'), description=_(u'help_emails_table', default=u'Add name and email by language'), value_type=DictRow(title=_(u'help_email_table'), schema=ITableEmailContact), required=False))
                        api.portal.set_registry_record(name='genweb.controlpanel.interface.IGenwebControlPanelSettings.contact_emails_table', value=old_values)

        if IAMGENWEBUPC:

            if create_packet:
                portal = getSite()
                # Reset, erase previous packets
                if getattr(portal['ca'], 'informacio-general', False):
                    portal.manage_delObjects('informacio-general')
                if getattr(portal['es'], 'informacion-general', False):
                    portal.manage_delObjects('informacion-general')
                if getattr(portal['en'], 'general-information', False):
                    portal.manage_delObjects('general-information')

                # Com que ja no existeix, el creem
                info_ca = self.create_content(portal['ca'], 'packet', 'informacio-general', title=u"informacio-general")
                info_ca.title = u"Informació general del màster"
                info_es = self.create_content(portal['es'], 'packet', 'informacion-general', title=u"informacion-general")
                info_es.title = u"Información general del máster"
                info_en = self.create_content(portal['en'], 'packet', 'general-information', title=u"general-information")
                info_en.title = u"General information on the master's degree"

                self.link_translations([(info_ca, 'ca'), (info_es, 'es'), (info_en, 'en')])

                adapter = getAdapter(info_ca, IpacketDefinition, 'fitxa_master')
                field_values = {u'codi_master': data['idestudi_master']}
                adapter.packet_fields = field_values
                adapter.packet_type = 'fitxa_master'
                adapter.packet_mapui = adapter.mapui
                alsoProvides(info_ca, IProtectedContent)

                adapter = getAdapter(info_es, IpacketDefinition, 'fitxa_master')
                field_values = {u'codi_master': data['idestudi_master']}
                adapter.packet_fields = field_values
                adapter.packet_type = 'fitxa_master'
                adapter.packet_mapui = adapter.mapui
                alsoProvides(info_es, IProtectedContent)

                adapter = getAdapter(info_en, IpacketDefinition, 'fitxa_master')
                field_values = {u'codi_master': data['idestudi_master']}
                adapter.packet_fields = field_values
                adapter.packet_type = 'fitxa_master'
                adapter.packet_mapui = adapter.mapui
                alsoProvides(info_en, IProtectedContent)

                info_ca.reindexObject()
                info_en.reindexObject()
                info_es.reindexObject()

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
