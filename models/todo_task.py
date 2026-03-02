
from odoo import models, fields, api

class TodoStage(models.Model): 
    _name = "todo.stage"
    _description = "Todo Stage"
    _order = "sequence, id"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)

    @api.model
    def get_dashboard_data(self):
        total = self.search_count([])
        todo = self.search_count([('stage_id.name', '=', 'To Do')])
        progress = self.search_count([('stage_id.name', '=', 'In Progress')])
        done = self.search_count([('stage_id.name', '=', 'Done')])

        return {
            'total': total,
            'todo': todo,
            'progress': progress,
            'done': done,
        }

class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo Task"
    _order = "sequence, id desc"

    name = fields.Char(string="Task", required=True)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date")
    sequence = fields.Integer(default=10)

    stage_id = fields.Many2one(
        "todo.stage",
        string="Stage",
        default=lambda self: self.env.ref("todo_app.todo_stage_todo", raise_if_not_found=False),
        index=True,
        store=True,
        ondelete="restrict",
    )