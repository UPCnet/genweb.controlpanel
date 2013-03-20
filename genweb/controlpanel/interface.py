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
                  fields=['contacte_id', 'contacte_BBDD_or_page', 'contacte_al_peu',
                          'directori_upc', 'contacte_no_upcmaps'])

    model.fieldset('Specific',
                  _(u'Specific'),
                  fields=['especific1', 'especific2',
                          'treu_imatge_capsalera', 'treu_menu_horitzontal',
                          'treu_icones_xarxes_socials', 'amaga_identificacio',
                          'idiomes_google_translate_link_ca', 'idiomes_google_translate_link_es',
                          'idiomes_google_translate_link_en'])

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
                default=u"És el literal que apareix al peu de pàgina o el text alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
    )

    signatura_unitat_es = schema.TextLine(
        title=_(u"signatura_unitat_es",
                default=u"Signatura de la unitat [ES]"),
        description=_(u"help_signatura_unitat_es",
                default=u"És el literal que apareix al peu de pàgina o el text alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
    )

    signatura_unitat_en = schema.TextLine(
        title=_(u"signatura_unitat_en",
                default=u"Signatura de la unitat [EN]"),
        description=_(u"help_signatura_unitat_en",
                default=u"És el literal que apareix al peu de pàgina o el text alternatiu del logotip (centres docents)."),
        required=False,
        # default=False,
    )

    codi_altre_marca_ca = schema.TextLine(
        title=_(u"codi_altre_marca_ca",
                default=u"Codi altra marca [CA]"),
        description=_(u"help_codi_altre_marca_ca",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta de la capçalera."),
        required=False,
        # default=False,
    )

    codi_altre_marca_es = schema.TextLine(
        title=_(u"codi_altre_marca_es",
                default=u"Codi altra marca [ES]"),
        description=_(u"help_codi_altre_marca_es",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta de la capçalera."),
        required=False,
        # default=False,
    )

    codi_altre_marca_en = schema.TextLine(
        title=_(u"codi_altre_marca_en",
                default=u"Codi altra marca [EN]"),
        description=_(u"help_codi_altre_marca_en",
                default=u"Codi HTML amb l'enllaç i imatge de logotips a la dreta de la capçalera."),
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

    contacte_BBDD_or_page = schema.Bool(
        title=_(u"contacte_BBBDD_or_page",
                default=u"Página de contacte personalitzada"),
        description=_(u"help_contacte_BBBDD_or_page",
                default=u"Per defecte, la informació de contacte prové de la base de dades de SCP, sota petició."),
        required=False,
        default=False,
    )

    contacte_al_peu = schema.Bool(
        title=_(u"contacte_al_peu",
                default=u"Adreça de contacte al peu"),
        description=_(u"help_contacte_al_peu",
                default=u"La informació provinent de la base de dades de SCP es visualitzen al peu de la pàgina."),
        required=False,
        default=False,
    )

    directori_upc = schema.Bool(
        title=_(u"directori_upc",
                default=u"Directori UPC a les eines"),
        description=_(u"help_directori_upc",
                default=u"Es mostra l'enllaç al directori UPC a la barra d'eines La informació prové de la base de dades de SCP."),
        required=False,
        default=False,
    )

    contacte_no_upcmaps = schema.Bool(
        title=_(u"contacte_no_upcmaps",
                default=u"Contacte sense UPCmaps"),
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

    treu_imatge_capsalera = schema.Bool(
        title=_(u"treu_imatge_capsalera",
                default=u"Treu la imatge de la capçalera"),
        description=_(u"help_treu_imatge_capsalera",
                default=u"Treiem la imatge de la capçalera per ..."),
        required=False,
        default=False,
    )

    treu_menu_horitzontal = schema.Bool(
        title=_(u"treu_menu_horitzontal",
                default="Treu el menú horitzontal"),
        description=_(u"help_treu_menu_horitzontal",
                default=u"Treu el menú horitzontal ..."),
        required=False,
        default=False,
    )

    treu_icones_xarxes_socials = schema.Bool(
        title=_(u"treu_icones_xarxes_socials",
                default="Treu les icones per compartir en xarxes socials"),
        description=_(u"help_treu_icones_xarxes_socials",
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
