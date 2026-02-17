# Jhon Hammond’s Dream

*A Digital Ecosystem Simulation*

---

## Overview

Jhon Hammond’s Dream is a turn-based spatial evolutionary simulation running on a 2D toroidal grid.

Autonomous agents (*Animals*) interact locally with resources (*Food*) through movement, combat, reproduction, mutation, aging, and death.
No behaviors are scripted beyond core mechanics — complex dynamics emerge purely from local rules and selection pressure.

The simulation evolves in discrete turns and often produces:

* Generational arms races
* Trait specialization
* Population oscillations
* Lineage collapses
* Extinction events

---

# Core Concepts

## The World

* A fixed-size 2D grid `(W, H)`
* Toroidal topology (wrap-around movement)
* Each cell contains:

  * Nothing
  * One Food
  * One Animal

All interactions occur locally in the **immediate cross**:

```
(x-1, y)
(x+1, y)
(x, y-1)
(x, y+1)
```

No diagonals.

---

# Entities

## Food (Passive Resource)

### Attributes

```
energy
x, y
```

### Behavior

* Each turn:

  * `energy -= 1`
  * Removed if `energy <= 0`
* If eaten:

  * Animal gains `food.energy`
  * Food disappears
* When an animal dies:

  * It converts into Food
  * `food.energy = animal.energy at death`

Food decays, forming an energy sink.

---

## Animal (Active Agent)

### Attributes

```
hit
max_life
life
energy
threshold
vision
gen

cooldown_attack
cooldown_aging

x, y
```

### Trait Meaning

**hit**
Damage dealt to each adjacent enemy.

**max_life**
Base health at birth.

**life**

* Decreases from combat damage
* Decreases by 1 per turn (unless aging cooldown active)
* Death at `life <= 0`

**energy**

* Gained from eating
* Required for reproduction

**threshold**
Minimum energy required to reproduce.

**vision**
Food detection radius (Manhattan distance).

**gen**
Generation number.

* Initial animals: `gen = 0`
* Offspring: `gen = parent.gen + 1`

**cooldown_attack**
Prevents attacking while active.

**cooldown_aging**
Prevents life loss while active.

---

# Initialization

Inputs:

```
animal_units
food_units
life_range
hit_range
energy_range
vision_range
max_turns (optional)
```

### Animal Creation

For each initial animal:

```
max_life ∈ life_range
life = max_life
hit ∈ hit_range
threshold ∈ energy_range
vision ∈ vision_range
energy = threshold / 4
gen = 0
cooldown_attack = 0
cooldown_aging = 0
```

Placed randomly on empty cells.

### Food Creation

For each food unit:

```
energy ∈ energy_range
```

Placed randomly on empty cells.

---

# Turn Structure

Each turn consists of two synchronized phases.

---

# Phase I — Decision Phase

Each animal chooses an action:

1. If at least one adjacent animal exists → **ATTACK**
2. Else:

   * If food within `vision` → move 1 step toward nearest food
   * Else → move randomly (within immediate cross)

No state changes occur yet.

---

# Phase II — Action Phase

Actions resolve simultaneously.

---

## 1. Food Decay

All food:

```
energy -= 1
remove if <= 0
```

---

## 2. Movement Resolution

If multiple animals target the same cell:

* One random winner moves
* Others remain in place

Animals cannot move into occupied animal cells.

---

## 3. Eating

If an animal occupies a food cell:

```
animal.energy += food.energy
food removed
```

---

## 4. Combat

If `cooldown_attack == 0`:

* Animal deals `hit` damage to every adjacent animal.
* Damage accumulates.
* All damage applied simultaneously.

Example:

If A adjacent to B and C:

```
B.life -= A.hit
C.life -= A.hit
A.life -= (B.hit + C.hit)
```

If `cooldown_attack > 0`:

* Animal receives damage from neighbors
* Does not deal damage
* `cooldown_attack -= 1`

Gang combat is possible.

---

## 5. Reproduction

Conditions:

* `energy >= threshold`
* No adjacent animals (not under attack)

### Process

1. Parent energy:

```
parent.energy = parent.energy / 2
```

2. Child energy:

```
child.energy = parent.energy / 4
```

3. Mutation (±1 drift):

For each:

```
max_life
hit
threshold
vision
```

```
child_trait = parent_trait + random(-1, 0, +1)
```

If any trait < 1:

* Child instantly converts to food.

4. Placement:

* Must spawn in immediate cross.
* If only food adjacent:

  * Parent eats one food cell to clear space.
* If under attack:

  * Reproduction delayed.

5. Post-birth cooldown:

Parent:

```
cooldown_attack = 2
cooldown_aging = 2
```

Child:

```
life = max_life
gen = parent.gen + 1
cooldown_attack = 2
cooldown_aging = 2
```

---

## 6. Aging

If `cooldown_aging == 0`:

```
life -= 1
```

Cooldown counters decrement (min 0).

---

## 7. Death

If `life <= 0`:

* Animal removed
* Food created at location:

```
food.energy = animal.energy
```

Energy recycles.

---

# Termination

Simulation ends if:

* All animals extinct
* `max_turns` reached
* Manual stop

---

# Emergent Dynamics

Despite simple local rules, the system frequently produces:

* Energy circulation loops
* Combat clustering
* Trait arms races
* Generational wipeouts
* Meta shifts
* Evolutionary overfitting and collapse
* Stable lineages
* Sudden extinction events

Mutation is minimal (±1 integer drift), yet long-term runs produce extreme specialization and dramatic discontinuities.

---

# Design Principles

* Fully local interactions
* Simultaneous update model
* No global coordination
* Mutation is small but cumulative
* Energy decays to prevent infinite growth
* Vision limits omniscience
* Toroidal spatial topology

---

# Classification

This project can be viewed as:

* A discrete-time spatial evolutionary model
* With local combat mechanics
* Energy-based reproduction economy
* Mutation-driven drift
* Emergent macro-behavior from micro-rules

---

## Why This Exists

To observe what happens when:

* Mutation is small
* Rules are strict
* Interactions are local
* And survival is the only objective

No AI.
No scripts.
Just selection and time.
