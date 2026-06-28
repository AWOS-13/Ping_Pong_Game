# 🏓Ping Pong (Python Turtle)

A classic two-player Pong game built with Python's `turtle` graphics module. Two paddles, one bouncing ball, and live score tracking — first to rack up the most points wins (bragging rights only, for now 😉).

## 📂 Project Structure

```
.
├── main.py     # Game window setup, ball physics, collision detection, main loop
├── ball.py     # Ball class — shape, color, movement speed
├── paddle.py   # Paddle class — movement (up/down)
└── score.py    # Score class — score display for both players
```

## ✅ Requirements

- Python 3.x
- `turtle` module (included in the standard Python library)

## ▶️ How to Run

```bash
python main.py
```

## 🕹️ Controls

| Player | Paddle | Up | Down |
|--------|--------|----|------|
| Right (Player 1) | Blue | ↑ | ↓ |
| Left (Player 2)  | Red  | w | s |

## 🏆 Scoring

- If the ball passes the **left** paddle, the right player (s1) scores.
- If the ball passes the **right** paddle, the left player (s2) scores.
- The ball speeds up slightly with every paddle hit, and resets to the center after each point.

