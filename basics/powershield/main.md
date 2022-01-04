Powershielding is a technique where shield is pressed just before an attack hits the player's character. If a physical attack is powershielded, no shield damage is dealt and the player can preform some moves out of shield.  If a projectile is powershielded, the projectile will be reflected, deal half the damage, and the player can act immediately with an out-of-shield option.

## MECHANICS

### ACTION STATES

The many things a character can do are split into action states. They define and assign unique properties to whatever the character is doing. Sitting idle? That's Wait. In airdodge? EscapeAir. Hundreds of these states come together to create Melee as we know it, but the ones we're interested in have to do with shield: 


| ACTION STATE | DESCRIPTION |
| -- | -- |
| GuardOn | Shield is activated and is visually expanding |
| Guard | Shield is held |
| GuardOff | Shield is turned off. The character goes through a 15 frame animation where they drop their guard |
| GuardDamage | Shieldstun |
| GuardReflect | The powershield sphere is activated. Physical attacks can be powershielded within the first four frames of activation, and projectiles can be reflected within the first two frames of activation |


### DIGITAL POWERSHIELDS

DK immediately enters GuardReflect when a digital input is used to shield.

![DPS](https://i.imgur.com/h0OLr22.png)

If a physical attack connects with the powershield sphere, the powershield will activate and DK will enter GuardDamage. As soon as GuardDamage is complete, and shield isn't held, DK will enter GuardOff. Because DK powershielded the attack, they can cancel the usual 15 frames of GuardOff with any action that uses A, B, X, Y, Z, or the c-stick. 

If a projectile connects with the powershield sphere, the projectile will be reflected and deal half its original damage. DK will remain in GuardReflect which can be immediately canceled into any standard OOS option.

### ANALOGUE DIGITAL POWERSHIELDS

Notice tat the digital powershield sphere doesn't completely cover DK's hurtbox. It sucks. One way to mitigate this flaw is to use analouge digital transition (ADT) powershields.

![adtps](https://i.imgur.com/k3EORuk.png)

A lot goes into preforming an ADT powershield. it's more efficient to lay it out and explain each piece independently 

| FRAME | INPUT | ACTION STATE | DESCRIPTION | 
| -- | -- | -- | -- |
| 1 | analogue shield | GuardOn | Shield sphere is activated. Acts like a normal shield | 
| 2 | digital shield | GuardReflect | Analogue shield transitions to a digital shield. Projectiles are reflected, physical attacks aren't blocked |
| 3 | digital shield | GuardReflect | Projectiles are reflected, physical attacks aren't blocked |
| 4 | digital shield | GuardReflect | Physical attacks are powershielded | 
| 5 | digital shield | GuardReflect | Physical attacks are powershielded | 

On frame 1, an analogue shield is input and DK enters GuardOn. If the shield sphere connects with an attack during this frame the next step will not work. On frame 2, a digital shield is input and DK enters GuardReflect. The powershield sphere is activated and is significantly larger than a normal digital powershield sphere. The shield sphere that blocks physical attacks is deactivated. This behavior continues to frame 3 until it returns to normal on frame 4.

The formula that calculates the size of an ADT powershield sphere is described as the following: 

![adt-formula](https://i.imgur.com/DpaYne8.png)

### NOTE

This is the first version of How to Powershield. I'm planning to edit this a ton and add more powershield shenanigans later.

