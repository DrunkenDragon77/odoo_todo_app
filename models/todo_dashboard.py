from odoo import models, fields, api

class TodoDashboard(models.Model):
    _name = "todo.dashboard"
    _description = "Todo Dashboard"

    name = fields.Char(default="Dashboard")

    total_count = fields.Integer(compute="_compute_counts")
    todo_count = fields.Integer(compute="_compute_counts")
    doing_count = fields.Integer(compute="_compute_counts")
    done_count = fields.Integer(compute="_compute_counts")

    @api.depends()
    def _compute_counts(self):
        Task = self.env["todo.task"]
        for rec in self:
            rec.total_count = Task.search_count([])

            # Using XML IDs of default stages (created in todo_stage.xml)
            todo_stage = self.env.ref("todo_app.todo_stage_todo", raise_if_not_found=False)
            doing_stage = self.env.ref("todo_app.todo_stage_doing", raise_if_not_found=False)
            done_stage = self.env.ref("todo_app.todo_stage_done", raise_if_not_found=False)

            rec.todo_count = Task.search_count([("stage_id", "=", todo_stage.id)]) if todo_stage else 0
            rec.doing_count = Task.search_count([("stage_id", "=", doing_stage.id)]) if doing_stage else 0
            rec.done_count = Task.search_count([("stage_id", "=", done_stage.id)]) if done_stage else 0
    def action_open_analysis(self):
        return self.env.ref("todo_app.action_todo_task_analysis").read()[0]
    def action_open_tasks(self):
        return {
            "type": "ir.actions.act_window",
            "name": "All Tasks",
            "res_model": "todo.task",
            "view_mode": "kanban,list,form",
        }

    def action_open_todo(self):
        stage = self.env.ref("todo_app.todo_stage_todo", raise_if_not_found=False)
        return self._open_stage(stage, "Todo Tasks")

    def action_open_doing(self):
        stage = self.env.ref("todo_app.todo_stage_doing", raise_if_not_found=False)
        return self._open_stage(stage, "Doing Tasks")

    def action_open_done(self):
        stage = self.env.ref("todo_app.todo_stage_done", raise_if_not_found=False)
        return self._open_stage(stage, "Done Tasks")

    def _open_stage(self, stage, title):
        domain = [("stage_id", "=", stage.id)] if stage else []
        return {
            "type": "ir.actions.act_window",
            "name": title,
            "res_model": "todo.task",
            "view_mode": "kanban,list,form",
            "domain": domain,
        }