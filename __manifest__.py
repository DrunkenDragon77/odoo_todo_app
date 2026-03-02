{
    "name": "Todo App",
    "version": "1.0",
    "summary": "Simple Todo tasks",
    "category": "Productivity",
    "author": "You",
    "depends": ["base"],
    "data": [
        
        "security/ir.model.access.csv",
        "views/todo_stage.xml",
        "views/todo_dashboard_views.xml",
        "views/todo_task_views.xml",
        "views/todo_task_graph_views.xml",
        "views/menu.xml",
    ],
    "application": True,
    "installable": True,
}
