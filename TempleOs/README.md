# TempleOS Snake - HolyC Experiment

This is my personal experiment with TempleOS and HolyC.

I created a small Snake game running directly inside TempleOS. The source file is located at:

C:/Home/Snake.HC

I have not yet found a reliable way to export the source file alone, so for now the project is shared as a complete TempleOS virtual machine image.

## Running the project

Requires QEMU.

Start TempleOS with:

qemu-system-x86_64 -m 512 -hda templeos.qcow2 -boot c -audiodev driver=dsound,id=snd0 -machine pcspk-audiodev=snd0

When TempleOS starts, choose:

1 - Boot from C:

## Useful TempleOS commands

Navigate directories:

Cd("");

Move one directory level up:

..

Show directory contents:

Dir;

Search for a word in the file tree:

Find("");

Clear the screen:

DocClear;

## Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + Alt + T | Open a new command window |
| Ctrl + M | Open the main menu |
| Ctrl + D | Open the file manager |
| Ctr + Alt + F | Full screen |
| Esc | Close the current window / abort current task |

## Running the game

Inside TempleOS:

#include "Snake.HC";

This will load the Snake game.

## Notes

This project is an exploration of TempleOS and HolyC, experimenting with programming in a very different environment compared to modern operating systems.

The goal was not only to create a game, but also to learn about low-level programming, graphics, and working closer to the system.