# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from z3c.form import button
from zope.component import getUtilitiesFor
from plone.app.registry.browser import controlpanel
from souper.interfaces import ICatalogFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.component import getUtility
from Products.statusmessages.interfaces import IStatusMessage
from plone.supermodel import model
from genweb.core import GenwebMessageFactory as _
from genweb.core.utilities import IElasticSearch

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

    model.fieldset('General',
                   (u'General'),
                   fields=['user_properties_extender',
                           'custom_editor_icons',
                           'elasticsearch'])

    model.fieldset('Ldap',
                   (u'Ldap'),
                   fields=['alt_ldap_uri',
                           'alt_bind_dn',
                           'alt_bindpasswd',
                           'alt_base_dn',
                           'groups_query',
                           'user_groups_query'])

    user_properties_extender = schema.Choice(
        title=_(u'User properties extender'),
        vocabulary=u'genweb.controlpanel.core.user_extenders',
        required=False,
        default=u''
    )

    custom_editor_icons = schema.List(
        title=_(u'Llista personalitzada d\'icones per l\'editor TinyMCE'),
        description=_(u'Cada línia és una fila d\'icones. Si es deixa en blanc s\'agafen els valors per defecte. Han d\'omplir-se fins a 4 files obligatòriament.'),
        value_type=schema.TextLine(),
        required=False,
        default=[]
    )

    elasticsearch = schema.TextLine(
        title=_(u"elasticsearch",
                default=u"ElasticSearch"),
        description=_(u"elasticsearch_help",
                      default=u"URL del servidor d'ElasticSearch per aquest site"),
        required=False,
        default=u'localhost',
    )

    alt_ldap_uri = schema.TextLine(
        title=_(u"alt_ldap_uri",
                default=u"alt_ldap_uri"),
        description=_(u"alt_ldap_uri_help",
                      default=u"URL del servidor ldap per aquest site"),
        required=False,
        default=u'',
    )

    alt_bind_dn = schema.TextLine(
        title=_(u"alt_bind_dn",
                default=u"alt_bind_dn"),
        description=_(u"alt_bind_dn_help",
                      default=u"LDAP bind dn"),
        required=False,
        default=u'',
    )

    alt_bindpasswd = schema.TextLine(
        title=_(u"alt_bindpasswd",
                default=u"alt_bindpasswd"),
        description=_(u"alt_bindpasswd_help",
                      default=u"LDAP bind password"),
        required=False,
        default=u'',
    )

    alt_base_dn = schema.TextLine(
        title=_(u"alt_base_dn",
                default=u"alt_base_dn"),
        description=_(u"alt_base_dn_help",
                      default=u"LDAP base dn"),
        required=False,
        default=u'',
    )

    groups_query = schema.TextLine(
        title=_(u"groups_query",
                default=u"groups_query"),
        description=_(u"groups_query_help",
                      default=u"LDAP groups query. Ex: (&(objectClass=groupOfNames))"),
        required=False,
        default=u'',
    )

    user_groups_query = schema.TextLine(
        title=_(u"user_groups_query",
                default=u"user_groups_query"),
        description=_(u"user_groups_query_help",
                      default=u"LDAP user groups query. Ex: (&(objectClass=groupOfNames)(member=%s))"),
        required=False,
        default=u'',
    )


class GenwebCoreControlPanelSettingsForm(controlpanel.RegistryEditForm):
    """ Genweb settings form """

    schema = IGenwebCoreControlPanelSettings
    id = "GenwebCoreControlPanelSettingsForm"
    label = _(u"Genweb Core")
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

        es = getUtility(IElasticSearch)
        es.create_new_connection()

        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"), "info")
        self.context.REQUEST.RESPONSE.redirect("@@genweb-core-controlpanel")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"), "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))


class GenwebCoreControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Genweb Core settings control panel """
    form = GenwebCoreControlPanelSettingsForm
