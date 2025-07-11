
## 1. Hospital Triage System
This project simulates a **patient queue** using a simple linked list, prioritizing patients with a **Yellow card (A)** (more urgent) over those with a **Green card (V)** (less urgent).

- **Yellow card (A)**: higher priority, numbering starts at 201  
- **Green card (V)**: lower priority, numbering starts at 1  
- Interactive menu to add patients, view the queue, and call the next patient


## 2. Vehicle Plate Hash Table
This project implements a hash table with separate chaining to map Brazilian vehicle plates to their registration states.

- Uses 10 linked lists (one for each hash position).
- Special hash function: returns 7 for “DF” and otherwise uses ASCII sum modulo 10.
- Inserts all 26 Brazilian states + Federal District and one fictional state.
- Prints the table showing the state codes stored in each position.
