# -*- coding: utf-8 -*-
from zope import schema
from plone.supermodel import model

from genweb.core import GenwebMessageFactory as _


class IGenwebControlPanelSettings(model.Schema):
    """ Global Genweb settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    model.fieldset('General',
                  _(u'General'),
                  fields=['extended_html_title'])

    model.fieldset('Contact information',
                  _(u'Contact information'),
                  fields=['contacteid'])

    # form.fieldset('Specific',
    #               _(u'Specific'),
    #               fields=[''])

    # form.fieldset('Master',
    #               _(u'Master'),
    #               fields=[''])

    extended_html_title = schema.TextLine(
        title=_(u"Header title with html tags",
                default=u"Header title with html tags"),
        description=_(u"help_globally_enabled",
                default=u"If selected, users are able to post comments on the "
                         "site. Though, you have to enable comments for "
                         "specific content types, folders or content objects "
                         "before users will be able to post comments."),
        required=False,
        # default=False,
        )

    contacteid = schema.TextLine(
        title=_(u"contact_id",
                default=u"Globally enable comments"),
        description=_(u"help_globally_enabled",
                default=u"If selected, users are able to post comments on the "
                         "site. Though, you have to enable comments for "
                         "specific content types, folders or content objects "
                         "before users will be able to post comments."),
        required=False,
        # default=False,
        )

    # anonymous_comments = schema.Bool(
    #     title=_(u"label_anonymous_comments",
    #             default="Enable anonymous comments"),
    #     description=_(u"help_anonymous_comments",
    #             default=u"If selected, anonymous users are able to post "
    #                      "comments without loggin in. It is highly "
    #                      "recommended to use a captcha solution to prevent "
    #                      "spam if this setting is enabled."),
    #     required=False,
    #     default=False,
    #     )

    # moderation_enabled = schema.Bool(
    #     title=_(u"label_moderation_enabled",
    #             default="Enable comment moderation"),
    #     description=_(u"help_moderation_enabled",
    #             default=u"If selected, comments will enter a 'Pending' state "
    #                      "in which they are invisible to the public. A user "
    #                      "with the 'Review comments' permission ('Reviewer' "
    #                      "or 'Manager') can approve comments to make them "
    #                      "visible to the public. If you want to enable a "
    #                      "custom comment workflow, you have to go to the "
    #                      "types control panel."),
    #     required=False,
    #     default=False,
    #     )

    # text_transform = schema.Choice(
    #     title=_(u"label_text_transform",
    #             default="Comment text transform"),
    #     description=_(u"help_text_transform",
    #             default=u"Use this setting to choose if the comment text " +
    #                      "should be transformed in any way. You can choose "
    #                      "between 'Plain text' and 'Intelligent text'. " +
    #                      "'Intelligent text' converts plain text into HTML " +
    #                      "where line breaks and indentation is preserved, " +
    #                      "and web and email addresses are made into " +
    #                      "clickable links."),
    #     required=True,
    #     default='text/plain',
    #     vocabulary='plone.app.discussion.vocabularies.TextTransformVocabulary',
    #     )

    # captcha = schema.Choice(
    #     title=_(u"label_captcha",
    #             default="Captcha"),
    #     description=_(u"help_captcha",
    #             default=u"Use this setting to enable or disable Captcha "
    #                      "validation for comments. Install "
    #                      "plone.formwidget.captcha, "
    #                      "plone.formwidget.recaptcha, collective.akismet, or "
    #                      "collective.z3cform.norobots if there are no options "
    #                      "available."),
    #     required=True,
    #     default='disabled',
    #     vocabulary='plone.app.discussion.vocabularies.CaptchaVocabulary',
    #     )

    # show_commenter_image = schema.Bool(
    #     title=_(u"label_show_commenter_image",
    #             default=u"Show commenter image"),
    #     description=_(u"help_show_commenter_image",
    #             default=u"If selected, an image of the user is shown next to "
    #                      "the comment."),
    #     required=False,
    #     default=True,
    #     )

    # moderator_notification_enabled = schema.Bool(
    #     title=_(u"label_moderator_notification_enabled",
    #             default=u"Enable moderator email notification"),
    #     description=_(u"help_moderator_notification_enabled",
    #             default=u"If selected, the moderator is notified if a comment "
    #                      "needs attention. The moderator email address can " +
    #                      "be found in the 'Mail settings' control panel "
    #                      "(Site 'From' address)"),
    #     required=False,
    #     default=False,
    #     )

    # moderator_email = schema.ASCIILine(
    #     title=_(u'label_moderator_email',
    #               default=u'Moderator Email Address'),
    #     description=_(u'help_moderator_email',
    #                   default=u"Address to which moderator notifications "
    #                           u"will be sent."),
    #     required=False,
    #     )

    # user_notification_enabled = schema.Bool(
    #     title=_(u"label_user_notification_enabled",
    #     default=u"Enable user email notification"),
    #     description=_(u"help_user_notification_enabled",
    #                   default=u"If selected, users can choose to be notified "
    #                            "of new comments by email."),
    #     required=False,
    #     default=False)
