# Snake-Game
A classic Snake Game built using Python’s turtle module. The game features smooth movement, random food generation, score tracking, and game-over detection when the snake hits the wall or collides with itself. The project follows an object-oriented design with separate modules for the snake, food, and scoreboard.

### 📁 File Overview

* **main.py**
  Controls the game loop, screen setup, collision detection, and keyboard input.

* **snake.py**
  Handles snake creation, movement, direction control, growth, and self-collision detection.

* **food.py**
  Creates food objects and places them randomly on the screen when eaten.

* **scoreboard.py**
  Displays the current score and shows the *GAME OVER* message.

---

### 🎮 How the Game Works

* The snake moves continuously on the screen.
* The player controls the snake using arrow keys.
* When the snake eats food:

  * The snake grows longer
  * The score increases
  * New food appears at a random location
* The game ends if:

  * The snake hits the screen boundary
  * The snake collides with its own body

---

### ⌨️ Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| ←   | Move Left  |
| →   | Move Right |

---

### 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in `turtle`)

---

### ▶️ Run the Game

```bash
python main.py
```

📸 Screenshots

* Game Start : Shows the initial state of the game with the snake and food positioned randomly.
* Gameplay : The snake grows as it eats food and the score increases in real time.
* Game Over : The game ends when the snake collides with the wall or its own body, displaying the final score and a GAME OVER message.

  

<img width="752" height="781" alt="snake score=3" src="https://github.com/user-attachments/assets/beff5599-d325-4467-aa13-a5ed84db401d" />


<img width="750" height="780" alt="snake start" src="https://github.com/user-attachments/assets/221a08c4-dff9-4a59-9886-b7cdf94c6109" />


<img width="790" height="784" alt="snake_gameover" src="https://github.com/user-attachments/assets/aada7244-8199-4176-b2ed-4687164cbfee" />

