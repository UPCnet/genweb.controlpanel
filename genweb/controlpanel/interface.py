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
                  fields=['html_title_ca', 'html_title_es', 'html_title_en',
                          'signatura_unitat_ca', 'signatura_unitat_es', 'signatura_unitat_en',
                          'codi_altre_marca_ca', 'codi_altre_marca_es', 'codi_altre_marca_en'])

    model.fieldset('Contact information',
                  _(u'Contact information'),
                  fields=['contacte_id', 'contacte_BBBDD_or_page', 'contacte_al_peu',
                          'directori_upc', 'contacte_no_upcmaps'])

    model.fieldset('Specific',
                  _(u'Specific'),
                  fields=['especific1', 'especific2',
                          'contrast_colors_bn', 'imatge_capsalera', 'menu_horitzontal',
                          'icones_xarxes_socials', 'amaga_identificacio',
                          'idiomes_google_translate_link_ca', 'idiomes_google_translate_link_es', 'idiomes_google_translate_link_en'])

    model.fieldset('Master',
                  _(u'Master'),
                  fields=['idestudi_master'])

    # General section

    html_title_ca = schema.TextLine(
        title=_(u"html_title_ca",
                default=u"Títol del web amb HTML tags (negretes) [CA]"),
        description=_(u"help_html_title_ca",
                default=u"Afegiu el títol del Genweb. Podeu incloure tags HTML"),
        required=False,
        # default=False,
        )

    html_title_es = schema.TextLine(
        title=_(u"html_title_es",
                default=u"Títol del web amb HTML tags (negretes) [ES]"),
        description=_(u"help_html_title_es",
                default=u"Afegiu el títol del Genweb. Podeu incloure tags HTML"),
        required=False,
        # default=False,
        )

    html_title_en = schema.TextLine(
        title=_(u"html_title_en",
                default=u"Títol del web amb HTML tags (negretes) [EN]"),
        description=_(u"help_html_title_en",
                default=u"Afegiu el títol del Genweb. Podeu incloure tags HTML."),
        required=False,
        # default=False,
        )

    signatura_unitat_ca = schema.TextLine(
        title=_(u"signatura_unitat_ca",
                default=u"Signatura de la unitat [CA]"),
        description=_(u"help_signatura_unitat_ca",
                default=u"És el literal que apareix al peu de pàgina o el text "
                         "alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
        )

    signatura_unitat_es = schema.TextLine(
        title=_(u"signatura_unitat_es",
                default=u"Signatura de la unitat [ES]"),
        description=_(u"help_signatura_unitat_es",
                default=u"És el literal que apareix al peu de pàgina o el text "
                         "alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
        )

    signatura_unitat_en = schema.TextLine(
        title=_(u"signatura_unitat_en",
                default=u"Signatura de la unitat [EN]"),
        description=_(u"help_signatura_unitat_en",
                default=u"És el literal que apareix al peu de pàgina o el text "
                         "alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
        )

    codi_altre_marca_ca = schema.TextLine(
        title=_(u"codi_altre_marca_ca",
                default=u"Codi altre marca [CA]"),
        description=_(u"help_codi_altre_marca_ca",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta "
                         "de la capçalera."),
        required=False,
        # default=False,
        )

    codi_altre_marca_es = schema.TextLine(
        title=_(u"codi_altre_marca_es",
                default=u"Codi altre marca [ES]"),
        description=_(u"help_codi_altre_marca_es",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta "
                         "de la capçalera."),
        required=False,
        # default=False,
        )

    codi_altre_marca_en = schema.TextLine(
        title=_(u"codi_altre_marca_en",
                default=u"Codi altre marca [EN]"),
        description=_(u"help_codi_altre_marca_en",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta "
                         "de la capçalera."),
        required=False,
        # default=False,
        )

    # Contact Information section

    contacte_id = schema.TextLine(
        title=_(u"contacte_id",
                default=u"ID contacte de la unitat"),
        description=_(u"help_contacte_id",
                default=u"Afegiu el id de contacte de la base de dades de màsters."),
        required=False,
        # default=False,
        )

    contacte_BBBDD_or_page = schema.Bool(
        title=_(u"contacte_BBBDD_or_page",
                default="Página de contacte personalitzada"),
        description=_(u"help_contacte_BBBDD_or_page",
                default=u"Per defecte, la informació de contacte prové de la base "
                         "de dades de SCP, sota petició."),
        required=False,
        default=False,
        )

    contacte_al_peu = schema.Bool(
        title=_(u"contacte_al_peu",
                default="Adreça de contacte al peu"),
        description=_(u"help_contacte_al_peu",
                default=u"La informació provinent de la base de dades de SCP "
                         "es visualitzen al peu de la pàgina."),
        required=False,
        default=False,
        )

    directori_upc = schema.Bool(
        title=_(u"directori_upc",
                default="Directori UPC a les eines"),
        description=_(u"help_directori_upc",
                default=u"Es mostra l'enllaç al directori UPC a la barra d'eines "
                         "La informació prové de la base de dades de SCP."),
        required=False,
        default=False,
        )

    contacte_no_upcmaps = schema.Bool(
        title=_(u"contacte_no_upcmaps",
                default="Contacte sense UPCmaps"),
        description=_(u"help_contacte_no_upcmaps",
                default=u"Es mostra la informació d'UPCmaps al contacte."),
        required=False,
        default=False,
        )

    # Specific section

    especific1 = schema.TextLine(
        title=_(u"especific1",
                default=u"Color específic 1"),
        description=_(u"help_especific1",
                default=u"Afegiu el color específic 1. És aquell que..."),
        required=False,
        # default=False,
        )

    especific2 = schema.TextLine(
        title=_(u"especific2",
                default=u"Color específic 2"),
        description=_(u"help_especific2",
                default=u"Afegiu el color específic 2. És aquell que..."),
        required=False,
        # default=False,
        )

    contrast_colors_bn = schema.Bool(
        title=_(u"contrast_colors_bn",
                default=u"Contrast de colors blanc/negre"),
        description=_(u"help_contrast_colors_bn",
                default=u"El contrast de colors ..."),
        required=False,
        default=False,
        )

    imatge_capsalera = schema.Bool(
        title=_(u"imatge_capsalera",
                default=u"Treu la imatge de la capçalera"),
        description=_(u"help_imatge_capsalera",
                default=u"Treiem la imatge de la capçalera per ..."),
        required=False,
        default=False,
        )

    menu_horitzontal = schema.Bool(
        title=_(u"menu_horitzontal",
                default="Treu el menú horitzontal"),
        description=_(u"help_menu_horitzontal",
                default=u"Treu el menú horitzontal ..."),
        required=False,
        default=False,
        )

    icones_xarxes_socials = schema.Bool(
        title=_(u"icones_xarxes_socials",
                default="Treu les icones per compartir en xarxes socials"),
        description=_(u"help_icones_xarxes_socials",
                default=u"Treu les icones per compartir en xarxes socials ..."),
        required=False,
        default=False,
        )

    amaga_identificacio = schema.Bool(
        title=_(u"amaga_identificacio",
                default="Amaga de les eines l'enllaç d'identificació"),
        description=_(u"help_amaga_identificacio",
                default=u"Amaga de les eines l'enllaç d'identificació ..."),
        required=False,
        default=False,
        )

    idiomes_google_translate_link_ca = schema.Bool(
        title=_(u"idiomes_google_translate_link_ca",
                default=u"Habilitar l'enllaç a la traducció automàtica de Google Translate [CA]"),
        description=_(u"help_idiomes_google_translate_link_ca",
                default=u"Blabla ..."),
        required=False,
        default=False,
        )

    idiomes_google_translate_link_es = schema.Bool(
        title=_(u"idiomes_google_translate_link_es",
                default=u"Habilitar l'enllaç a la traducció automàtica de Google Translate [ES]"),
        description=_(u"help_idiomes_google_translate_link_es",
                default=u"Blabla ..."),
        required=False,
        default=False,
        )

    idiomes_google_translate_link_en = schema.Bool(
        title=_(u"idiomes_google_translate_link_en",
                default=u"Habilitar l'enllaç a la traducció automàtica de Google Translate [EN]"),
        description=_(u"help_idiomes_google_translate_link_en",
                default=u"Blabla ..."),
        required=False,
        default=False,
        )

    # Master section

    idestudi_master = schema.TextLine(
        title=_(u"idestudi_master",
                default=u"id_estudi"),
        description=_(u"help_idestudi_master",
                default=u"Afegiu el id de l'estudi de la base de dades de màsters."),
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
