odoo.define('ont_survey_web.tree_view_button_survey_oniad', function (require){
"use strict";
    var ListView = require('web.ListView');
    var Model = require('web.DataModel');
    var Dialog = require('web.Dialog');
    
    ListView.include({
        render_buttons: function() {
            this._super.apply(this, arguments)
            if (this.$buttons) {
                this.$buttons.find('.o_survey_user_input_pedir_llamada_button').on('click', this.proxy('survey_user_input_pedir_llamada_button'));
            }
        },
        survey_user_input_pedir_llamada_button: function() {
            new Model('survey.user_input')
                .call('action_boton_pedir_llamada', [[]])
                .then(function(result) {
                    if(result.errors==true)
                    {
                        Dialog.confirm(self, result.error, {
                            title: 'Error',
                        });                                                                        
                    }
                    else
                    {
                        location.reload();
                    }
                })
        },        
    });
});