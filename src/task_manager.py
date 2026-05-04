import json

DATA_FILE = "data/tasks.json"


def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks():
    tasks = load_tasks()
    print("\nDaftar Task:")
    for task in tasks:
        print(
            f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}"
        )


def add_task():
    tasks = load_tasks()

    new_id = max(task["id"] for task in tasks) + 1
    title = input("Judul task: ")
    description = input("Deskripsi: ")
    priority = input("Priority low/medium/high: ")
    assignee = input("Assignee: ")

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee,
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task berhasil ditambahkan.")


def update_status():
    tasks = load_tasks()
    try:
        task_id = int(input("Masukkan ID task: "))
        new_status = input("Status baru (todo/in_progress/done): ")

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                save_tasks(tasks)
                print("Status berhasil diubah.")
                return
        print("Task tidak ditemukan.")
    except ValueError:
        print("Input ID harus berupa angka.")


def delete_task():
    tasks = load_tasks()
    try:
        task_id = int(input("Masukkan ID task yang akan dihapus: "))
        new_tasks = [task for task in tasks if task["id"] != task_id]

        if len(new_tasks) == len(tasks):
            print(f"Task dengan ID {task_id} tidak ditemukan.")
        else:
            save_tasks(new_tasks)
            print(f"Task dengan ID {task_id} berhasil dihapus.")
    except ValueError:
        print("Error: Input ID harus berupa angka.")


def search_by_assignee():
    tasks = load_tasks()

    keyword = input("Masukkan nama assignee: ").lower()
    results = [task for task in tasks if keyword in task["assignee"].lower()]

    if not results:
        print("Task tidak ditemukan.")
    else:
        print("\nHasil pencarian:")
        for task in results:
            print(
                f"{task['id']}. {task['title']} | Status: {task['status']} | PIC:{task['assignee']}"
            )
