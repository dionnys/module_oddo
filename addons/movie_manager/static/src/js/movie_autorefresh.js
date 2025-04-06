odoo.define('movie_manager.auto_refresh', function (require) {
    "use strict";

    const ListController = require('web.ListController');
    const viewRegistry = require('web.view_registry');
    const ListView = require('web.ListView');

    const AutoRefreshListController = ListController.extend({
        start() {
            this._super(...arguments);
            this._autoRefresh();
        },
        _autoRefresh() {
            setInterval(() => {
                this.reload();  // Recarga la vista
            }, 60000); // Cada 60 segundos
        }
    });

    const AutoRefreshListView = ListView.extend({
        config: Object.assign({}, ListView.prototype.config, {
            Controller: AutoRefreshListController
        }),
    });

    viewRegistry.add('auto_refresh_list', AutoRefreshListView);
});
