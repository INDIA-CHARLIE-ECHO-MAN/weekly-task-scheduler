# weekly-task-scheduler
###
This python project is to make an application that allows the user to create tasks for themselves and assign them to the days of the week.
When they have finished the tasks, they can close the task and the task will appear in a list of closed tasks of that day. 
They can delete the tasks they have made, or organise all the tasks from an open tasks panel. 
###
# flowchart of potential functions of the app
![image](https://user-images.githubusercontent.com/43439611/119513654-bfd4ef00-bdb7-11eb-9eea-ec6c730fcc26.png)
# flowchart of functions required to implement the potential functions of the app
![image](https://user-images.githubusercontent.com/43439611/119513677-c499a300-bdb7-11eb-82a0-a25629468d81.png)

# Table for Backend functions
| Description | Data type| Exceptions |
| --- | --- | --- | 
| Add task | Parameters:<li>task(str)<li>list(str)<br>Return Values:<li>NULL | Invalid task input<br>Invalid list input |
| Delete task | Parameters:<li>index(int)<li>list(str)<br>Return Values:<li>NULL | Invalid task input<br>Invalid list input |
| Assign task | Parameters:<li>index(str)<li>origin(str)<li>to(str)<br>Return Values:<li>NULL | Invalid index input<br>Invalid list input |
| Rearrange task | Parameters:<li>init_pos(str)<li>fin_pos(int)<li>panel(str)<br>Return Values:<li>NULL | Invalid index input<br>Invalid panel input |
| Reset schedule | Parameters:<li>NULL<br>Return Values:<li>NULL | NULL |
