# astar3D

![Example](img/example.gif)

## About
This project is a visualization of the A* algorithm in 3D. 
The location, including the start and end points, is generated randomly. 
User can increase the number of barriers at runtime. 
Visualization part of this project was implemented using `ursina` library.

This project is a reworked version of my semester work 
for the course Artificial Intelligence Fundamentals in the academic year 2022/2023.

## Features and control
* After launching the application, 
you can move inside the location using keys **W**, **A**, **S**, **D** keys and jump using the **Spacebar**. 
The **blue cube** represents the **start point**, and the **pink cube** represents the **end point**.

* To fully regenerate the location, you can press the **1** key on your keyboard. 
All barriers, the start point, and the end point will be regenerated.

* If you want to add more barriers, you can press (or hold) the **2** key on your keyboard, 
and barriers will be generated. The number of barriers is displayed at the top of the screen.

* To find the path from the start point (blue cube) to the end point (pink cube), press the **Enter** key. 
After pressing it, the path will be drawn using green cubes, or you will see a warning message if the path is not found.

* To exit, press the **Escape** key.


## How run
* Install all library's and packages

>[NOTE] User's PC must have already installed python 3.11 or higher.

```shell 
pip install -r requirements.txt
```
* Go to `src` folder.

```shell
cd src
```

* Run application.

```shell
python main.py
```