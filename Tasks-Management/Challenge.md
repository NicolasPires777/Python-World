# Python Challenge - Task Management System with Prioritization

## Challenge Description

In this challenge, you will develop a simple task management system where each task has a **name**, a **due date**, and a **priority level** (low, medium, high). The goal is to create a Python program that allows users to add, list, remove, filter, and update tasks, while saving the data in a JSON file.

## Requirements

1. **Add Task**: The user should be able to add new tasks with:
   - Task name
   - Due date (in the format `dd/mm/yyyy`)
   - Priority level (low, medium, high)
   
2. **List Tasks**: The system should display tasks organized by:
   - **Priority**: High-priority tasks should be listed first, followed by medium and low-priority tasks.
   - **Due Date**: Within each priority level, tasks should be ordered from the nearest to the farthest due date.

3. **Remove Task**: The user should be able to remove tasks by the task name.

4. **Filter Tasks**: The system should allow filtering tasks by priority level, showing only tasks with the selected priority (low, medium, or high).

5. **Update Task**: The user should be able to update the name, due date, or priority of an existing task.

6. **Save and Load Data**: The system should save tasks to a JSON file, and when restarting the program, tasks should be loaded automatically from the file.

## Usage Example

```python
# Adding tasks
add_task("Buy milk", "17/10/2024", "high")
add_task("Study Python", "18/10/2024", "medium")
add_task("Exercise", "17/10/2024", "low")

# Listing tasks
list_tasks()
# Output:
# 1. Buy milk - 17/10/2024 - Priority: High
# 2. Study Python - 18/10/2024 - Priority: Medium
# 3. Exercise - 17/10/2024 - Priority: Low

# Filtering high-priority tasks
filter_tasks_by_priority("high")
# Output:
# 1. Buy milk - 17/10/2024 - Priority: High
