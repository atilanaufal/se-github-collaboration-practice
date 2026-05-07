from src.task_manager import (
    get_all_tasks,
    add_task_data,
    update_task_status,
    delete_task_data,
    search_task_by_assignee,
)


def sample_tasks():
    return [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Desc",
            "status": "todo",
            "priority": "high",
            "assignee": "Rina",
        }
    ]


def test_get_all_tasks():
    tasks = sample_tasks()
    result = get_all_tasks(tasks)
    assert len(result) == 1


def test_add_task():
    tasks = sample_tasks()

    result = add_task_data(tasks, "Task Baru", "Testing", "medium", "Budi")

    assert len(result) == 2
    assert result[-1]["title"] == "Task Baru"


def test_update_task_status():
    tasks = sample_tasks()

    result = update_task_status(tasks, 1, "done")

    assert result[0]["status"] == "done"


def test_delete_task():
    tasks = sample_tasks()

    result = delete_task_data(tasks, 1)

    assert len(result) == 0


def test_search_task_by_assignee():
    tasks = sample_tasks()

    result = search_task_by_assignee(tasks, "rina")

    assert len(result) == 1
