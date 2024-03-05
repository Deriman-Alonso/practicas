from odoo import models, fields

class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Model for reporting Sports Issues"

    name = fiels.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string="Date")
    assistance = fields.Bool(string="Assistance")
    state = fields.Selection([('draft','Draft'),('open','Open'),('closed','Closed')],string="State",default="draft",)