# Web of the Dead: Nacht Prototype 🧟‍♂️🔦

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Tech](https://img.shields.io/badge/tech-HTML5%20Canvas%20%7C%20Vanilla%20JS-yellow)
![Platform](https://img.shields.io/badge/platform-Desktop%20%7C%20Mobile%20%7C%20Gamepad-green)

A single-file, browser-based recreation of the classic *World at War* "Nacht der Untoten" Zombies mode. Built entirely in Vanilla JavaScript and HTML5 Canvas with no external dependencies.

## 🎮 Play Now
Simply download the `index.html` file and open it in any modern web browser (Chrome, Firefox, Safari, Edge). No server or installation required.

---

## ✨ Features

### Core Gameplay
* **Round-Based Survival:** Infinite waves of zombies that grow stronger and faster (Health scales +10% per round).
* **Economy System:** Earn points by hitting (+10) and killing (+60/100) zombies to purchase weapons and unlock areas.
* **Health Regeneration:** "Bloody screen" damage indicators with auto-regeneration after 5 seconds.

### The "Nacht" Map
* **3 Unlockable Zones:**
    * *Spawn Room:* Kar98k, M1A1 Carbine.
    * *Help Room:* Thompson, Double-Barrel Shotgun, Mystery Box.
    * *Upstairs:* Sniper Cabinet, BAR, Sawed-Off Shotgun.
* **Interactive Windows:** Repair barricades to slow down zombies and earn points.
* **The Mystery Box:** Random weapon generator (includes the Ray Gun, Flamethrower, and more).

### Cross-Platform Controls
* **Desktop:** WASD + Mouse Aim.
* **Mobile:** Dual virtual joysticks + touch interactions (inspired by CoD Mobile).
* **Gamepad:** Full controller support via the HTML5 Gamepad API.

---

## 🕹️ Controls

| Action | Keyboard/Mouse | Gamepad (Xbox/PS) | Mobile Touch |
| :--- | :--- | :--- | :--- |
| **Move** | `W` `A` `S` `D` | Left Stick | Virtual Left Stick |
| **Aim** | Mouse Cursor | Right Stick | Virtual Right Stick |
| **Shoot** | Left Click | Right Trigger (R2) | Right Stick Button / Tap |
| **Interact / Buy** | `F` | `X` (Square) | Tap Context Icon |
| **Reload** | `R` | `X` (Square) | Tap Reload Icon |
| **Switch Weapon** | `Space` / `1`-`2` | `Y` (Triangle) | Tap Weapon Icon |
| **Melee** | `V` | Right Stick Click (R3) | Tap Melee Icon |
| **Pause** | `Esc` | `Start` (Options) | Pause Button |

---

## 🛠️ Technical Implementation

The entire game engine is contained within a single file for maximum portability.

### Architecture
* **Rendering:** HTML5 `<canvas>` Context 2D.
* **State Management:** Object-Oriented design with a central `Game` class managing the loop.
* **Entities:**
    * `Player`: Handles velocity, input mapping, and inventory.
    * `Zombie`: A* Pathfinding (or direct vector logic) with collision avoidance.
    * `Bullet`: Raycasting/Projectile logic depending on weapon type.
* **Audio:** Synthesized sound effects (Oscillators) or base64 encoded strings to maintain single-file structure.

### Project Structure
```text
index.html
├── <style> (CSS for UI overlays, HUD, and responsive canvas)
├── <canvas> (The game world)
└── <script> (All game logic)
    ├── Constants (Weapon stats, Map data)
    ├── Classes (Player, Zombie, Game)
    ├── Input Handlers (Touch, Mouse, Keyboard, Gamepad)
    └── Main Loop (requestAnimationFrame)
