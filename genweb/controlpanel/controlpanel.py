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
    label = _(u"Genweb settings")
    description = _(u"help_discussion_settings_editform",
                    default=u"Some discussion related settings are not "
                             "located in the Discussion Control Panel.\n"
                             "To enable comments for a specific content type, "
                             "go to the Types Control Panel of this type and "
                             "choose \"Allow comments\".\n"
                             "To enable the moderation workflow for comments, "
                             "go to the Types Control Panel, choose "
                             "\"Comment\" and set workflow to "
                             "\"Comment Review Workflow\".")

    def updateFields(self):
        super(GenwebControlPanelSettingsForm, self).updateFields()
        # self.fields['globally_enabled'].widgetFactory = \
        #     SingleCheckBoxFieldWidget
        # self.fields['moderation_enabled'].widgetFactory = \
        #     SingleCheckBoxFieldWidget
        # self.fields['anonymous_comments'].widgetFactory = \
        #     SingleCheckBoxFieldWidget
        # self.fields['show_commenter_image'].widgetFactory = \
        #     SingleCheckBoxFieldWidget
        # self.fields['moderator_notification_enabled'].widgetFactory = \
        #     SingleCheckBoxFieldWidget
        # self.fields['user_notification_enabled'].widgetFactory = \
        #     SingleCheckBoxFieldWidget

    def updateWidgets(self):
        super(GenwebControlPanelSettingsForm, self).updateWidgets()
        # self.widgets['globally_enabled'].label = _(u"Enable Comments")
        # self.widgets['anonymous_comments'].label = _(u"Anonymous Comments")
        # self.widgets['show_commenter_image'].label = _(u"Commenter Image")
        # self.widgets['moderator_notification_enabled'].label = \
        #     _(u"Moderator Email Notification")
        # self.widgets['user_notification_enabled'].label = \
        #     _(u"User Email Notification")

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect("@@discussion-settings")

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

#     def settings(self):
#         """Compose a string that contains all registry settings that are
#            needed for the discussion control panel.
#         """
#         registry = queryUtility(IRegistry)
#         settings = registry.forInterface(IGenwebControlPanelSettings, check=False)
#         wftool = getToolByName(self.context, "portal_workflow", None)
#         workflow_chain = wftool.getChainForPortalType('Discussion Item')
#         output = []

#         # Globally enabled
#         if settings.globally_enabled:
#             output.append("globally_enabled")

#         # Comment moderation
#         if 'one_state_workflow' not in workflow_chain and \
#         'comment_review_workflow' not in workflow_chain:
#             output.append("moderation_custom")
#         elif settings.moderation_enabled:
#             output.append("moderation_enabled")

#         # Anonymous comments
#         if settings.anonymous_comments:
#             output.append("anonymous_comments")

#         # Invalid mail setting
#         ctrlOverview = getMultiAdapter((self.context, self.request),
#                                        name='overview-controlpanel')
#         if ctrlOverview.mailhost_warning():
#             output.append("invalid_mail_setup")

#         # Workflow
#         wftool = getToolByName(self.context, 'portal_workflow', None)
#         if workflow_chain:
#             discussion_workflow = workflow_chain[0]
#             output.append(discussion_workflow)

#         # Merge all settings into one string
#         return ' '.join(output)

#     def mailhost_warning(self):
#         """Returns true if mailhost is not configured properly.
#         """
#         # Copied from plone.app.controlpanel/plone/app/controlpanel/overview.py
#         mailhost = getToolByName(aq_inner(self.context), 'MailHost', None)
#         if mailhost is None:
#             return True
#         mailhost = getattr(aq_base(mailhost), 'smtp_host', None)
#         email = getattr(aq_inner(self.context), 'email_from_address', None)
#         if mailhost and email:
#             return False
#         return True

#     def custom_comment_workflow_warning(self):
#         """Returns a warning string if a custom comment workflow is enabled.
#         """
#         wftool = getToolByName(self.context, "portal_workflow", None)
#         workflow_chain = wftool.getChainForPortalType('Discussion Item')
#         if 'one_state_workflow' in workflow_chain \
#         or 'comment_review_workflow' in workflow_chain:
#             return
#         return True

#     def unmigrated_comments_warning(self):
#         """Returns true if site contains unmigrated comments.
#         """
#         catalog = getToolByName(aq_inner(self.context), 'portal_catalog', None)
#         count_comments_old = catalog.searchResults(
#             object_provides=IDiscussionResponse.__identifier__)
#         if count_comments_old:
#             return True


# def notify_configuration_changed(event):
#     """Event subscriber that is called every time the configuration changed.
#     """
#     portal = getSite()
#     wftool = getToolByName(portal, 'portal_workflow', None)

#     if IRecordModifiedEvent.providedBy(event):
#         # Discussion control panel setting changed
#         if event.record.fieldName == 'moderation_enabled':
#             # Moderation enabled has changed
#             if event.record.value == True:
#                 # Enable moderation workflow
#                 wftool.setChainForPortalTypes(('Discussion Item',),
#                                               'comment_review_workflow')
#             else:
#                 # Disable moderation workflow
#                 wftool.setChainForPortalTypes(('Discussion Item',),
#                                               'one_state_workflow')

#     if IConfigurationChangedEvent.providedBy(event):
#         # Types control panel setting changed
#         if 'workflow' in event.data:
#             registry = queryUtility(IRegistry)
#             settings = registry.forInterface(IDiscussionSettings, check=False)
#             workflow_chain = wftool.getChainForPortalType('Discussion Item')
#             if workflow_chain:
#                 workflow = workflow_chain[0]
#                 if workflow == 'one_state_workflow':
#                     settings.moderation_enabled = False
#                 elif workflow == 'comment_review_workflow':
#                     settings.moderation_enabled = True
#                 else:
#                     # Custom workflow
#                     pass
