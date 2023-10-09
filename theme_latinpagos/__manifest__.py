# -*- coding: utf-8 -*-
# Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details

{
    'name': 'Theme Latinpagos',
    'category': 'Theme',
    'version': '16.0.0.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com',
    'summary': 'Theme Latinpagos',    
    'description': """Theme Latinpagos""",
    'depends': [
        'website',
        'website_crm',
        'website_helpdesk',
    ],

    'data': [
        'views/footer_one.xml',
        'views/header_one.xml',
        'views/theme_latinpagos_inherited.xml',

        # Snippets
        'views/snippets/s_index_fullpage.xml',
        'views/snippets/s_offer_fullpage.xml',
        'views/snippets/s_aboutus_fullpage.xml',
        'views/snippets/s_sales_fullpage.xml',
        'views/snippets/s_support_fullpage.xml',
        'views/snippets/s_medium_fullpage.xml',

        'views/snippets/s_about_banner.xml',
        'views/snippets/s_about_boost.xml',
        'views/snippets/s_about_img_text.xml',
        'views/snippets/s_about_img_text_two.xml',
        'views/snippets/s_about_mission.xml',
        'views/snippets/s_about_offers.xml',
        'views/snippets/s_about_payments.xml',

        'views/snippets/s_index_banner.xml',
        'views/snippets/s_index_ally.xml',
        'views/snippets/s_index_facility.xml',
        'views/snippets/s_index_financing.xml',
        'views/snippets/s_index_support.xml',
        'views/snippets/s_index_technology.xml',

        'views/snippets/s_offer_banner.xml',
        'views/snippets/s_offer_contact.xml',
        'views/snippets/s_offer_equipment.xml',
        'views/snippets/s_offer_equipment_two.xml',
        'views/snippets/s_offer_financing.xml',
        'views/snippets/s_offer_think.xml',

        'views/snippets/s_sales_banner.xml',
        'views/snippets/s_sales_applications.xml',
        'views/snippets/s_sales_collections.xml',
        'views/snippets/s_sales_business_partner.xml',
        'views/snippets/s_sales_equipment.xml',
        'views/snippets/s_sales_costs_one.xml',
        'views/snippets/s_sales_costs_two.xml',

        'views/snippets/s_support_banner.xml',
        'views/snippets/s_support_banner_two.xml',
        'views/snippets/s_support_medium.xml',
        'views/snippets/s_support_tabs.xml',
        'views/snippets/s_support_types.xml',

        'views/snippets/s_form_natural_person.xml',
        'views/snippets/s_form_legal_person.xml',
        'views/snippets/s_support_form_natural_person.xml',
        'views/snippets/s_support_form_legal_person.xml',
    ],

    'assets': {
        
        'web._assets_primary_variables':[
            "/theme_latinpagos/static/src/scss/theme_variable.scss",
        ],

        'web._assets_frontend_helpers': [
            "/theme_latinpagos/static/src/scss/bootstrap_overridden.scss",
        ],

        'web.assets_frontend': [
            "/theme_latinpagos/static/src/scss/fonts.scss",
            "/theme_latinpagos/static/src/scss/index_page.scss",
            "/theme_latinpagos/static/src/scss/footer.scss",
            "/theme_latinpagos/static/src/scss/header.scss",

            "/theme_latinpagos/static/src/js/header.js",
            "/theme_latinpagos/static/src/js/particles.js",
            "/theme_latinpagos/static/src/js/app.js",
        ],
    },


    'images': [
       'static/description/latinpagos_screenshot.png',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
}
