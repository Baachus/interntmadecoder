const listContainer = document.getElementById("list-container");

function addTask(){
    console.log("Adding Task...");

    // Global variables
    let task = document.getElementById("taskInput").value;
    const priority = document.getElementById("priority").value;

    // Remove whitespace
    task = task.trim();

    // Check if task is empty
    if (task == "") {
        alert("Please enter a task.");
        return;
    }

    // Modifiable variables
    const taskItem = document.createElement("li");
    const taskText = document.createElement("span");
    taskItem.classList.add("list-group-item");
    taskText.classList.add("task-text");
    taskText.textContent = task;

    const checkItem = document.createElement("input");
    checkItem.type = "checkbox";
    checkItem.classList.add("form-check-input");
    
    // Set ID and priority list for the new task
    taskItem.id = task;
    let taskList = document.getElementById("task-list-"+priority);

    // Add task to list
    taskItem.appendChild(checkItem);
    taskItem.appendChild(taskText);
    taskList.appendChild(taskItem);

    document.getElementById("taskInput").value = "";
}

listContainer.addEventListener("click", function(e){
    if(e.target.tagName==="INPUT" && e.target.type==="checkbox"){
        const listItem = e.target.parentNode;
        
        // Strike through task
        if(e.target.checked){
            listItem.style.textDecoration = "line-through";
        }
        else{
            listItem.style.textDecoration = "none";
        }

        // Remove task from list
        // const taskList = listItem.parentNode;
        // taskList.removeChild(listItem);
    }
});