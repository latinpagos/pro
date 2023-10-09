odoo.define('theme_latinpagos.headerjs', function (require) {
    'use strict';

    require('web.dom_ready');
    var ajax = require('web.ajax');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.mblheaderjs = publicWidget.Widget.extend({
        selector: "#wrapwrap",
        events: {
            'click #mbl_sidebar_toogler': '_OpenMblSideBar',
            'click .mbl-sidebar-backdrop': '_CloseMblSideBar',
        },
        _OpenMblSideBar: function (e) {
            $(".mbl-sidebar-content").addClass("active");
            e.stopPropagation()
        },
        _CloseMblSideBar: function (e) {
            $(".mbl-sidebar-content").removeClass("active");
            e.stopPropagation()
        },
    })
});