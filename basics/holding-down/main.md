---
title: "The Mechanics Of Crouch Cancelling"
---

\newpage 

There are so many different terms that are thrown around when people talk about crouch cancel. They're awful and don't do a good job describing what's actually happening on a mechanical level. Like, you can crouch cancel, but to do it you don't have to crouch, and if you do crouch it doesn't automatically mean you'll cancel your lag, but if you crouch and cancel your lag then it's a "true" crouch cancel. It's dumb. 

For the sake of this guide we'll get rid of them all and work with a couple new terms: land cancel (LC) and grounded land cancel (GLC).

# Land Cancels

If you are hit with a move in the air and are not in tumble, you can land on the ground and cancel the rest of your hitstun with your landing animation. The length of the landing animation varies from character to character, but the average is around 4 frames with a couple outliers (DK's is 5 frames long, Pichu's is 2 frames long, etc).

<!-- slow motion clip of a grounded and aerial waveshine -->

It's uses are endless, but that's not the point of this guide. We're interested in its variation: the grounded land cancel. 

The general idea behind a GLC is the same as an LC. The difference is that you use quirks of the physics engine to do it from the ground. The following conditions must be met to preform a GLC: 

1. the distance you ASDI down is greater than your initial vertical launch velocity
2. you're hit with a move with an upwards launch angle
3. you're hit with a move with less than 80 knockback

## Condition 1

A GLC is built on the fact that some moves launch you into the air, and you can use ASDI to teleport back down to cancel whatever hitstun you had with an LC. The game takes the vector of your initial launch velocity, adds the vector of your ASDI, and then uses that as your new position. All this happens in one frame.

<!-- clip of initial velocity and ASDI update priority  -->

It only works as long as the distance you're launched up is less than the distance you teleport back down. For reference, ASDI straight down moves your character by three in-game units. 

<!-- clips of ASDI down with different lengths -->

SDI can't be used to teleport back down. You can only SDI during hitlag and therefore can't interact with your initial launch velocity, so no matter how much you try to SDI down your environmental collision box will collide with the floor and the game will place you back on top.

<!-- clip of SDI down not working -->


## Condition 2

If you are on the ground and are not hit at an upwards angle it is impossible to ASDI or SDI vertically, making it impossible to GLC. This was a conscious design choice by the developers because they realized that, hey, all the meteors we spent so much time programming don't work if you just hold up.

Other edge cases are moves that have a Sakurai angle. If a move has a Sakurai angle, the angle it launches at will change depending on position and knockback dealt. 

![](https://i.imgur.com/NZOdx5Q.png)

If a grounded character is hit with a move that has a Sakurai angle and it deals a maximum of 32 knockback, they'll be launched at a horizontal angle, which makes it impossible to GLC. 

You can still LC a move without an upwards trajectory if you start in the air. 

<!-- clips of GLC vs LC on falco dair  -->

## Condition 3

When someone is launched into the air they can enter either non-tumble or tumble hitstun. If you hit the ground during non-tumble you'll land normally and preform and LC, but if you hit the ground while in tumble you'll be knocked down. A character enters tumble when they're hit with a move that deals at least 80 knockback. Therefore, a GLC can only be preformed against moves that deal less than 80 knockback.

Crossing the knockback threshold is the main bottleneck for preforming a GLC. You'll almost always pass over the 80 knockback mark before your initial vertical launch velocity is greater than the distance you ASDI down. It's the reason why you can still Amsah tech strong moves at high percents. 

\newpage

# Other Variables 

## Gray Stick and CStick ASDI 

You can input ASDI with the gray stick or the cstick. While they're functionally identical, which you choose will significantly impact what you can do during and after a GLC. While the gray stick is more convenient, you have to control your ASDI, crouch armor, SDI, DI, and movement with just one input device, but if you use the cstick that burden is spread across two input devices. 

If you use the gray stick for ASDI it's called a gray stick GLC. If you use the cstick for ASDI it's called a cstick GLC. The distinction will make sense in later sections. 

## Diagonal ASDI

Melee is an analogue game. You don't have to hold all the way down on the gray stick or cstick to preform a GLC. The only thing that matters is that the distance you travel down with ASDI down is greater than the distance you travel up from your initial vertical launch velocity. That extra leeway can be used to do diagonal ASDI.

Diagonal ASDI can change how far you travel horizontally during a GLC. 

<!-- comparison between different angles of asdi -->

You can use that extra boost to fight back against a move's pushback or to escape pressure. 

<!-- example of using diagonal asdi to escape pressure, example of diagonal asdi to fight pushback -->

## DI

DI changes your launch angle, and when your launch angle changes so does your initial vertical launch velocity, meaning that depending on how you DI a move you'll either decrease or increase the distance needed to ASDI down. 

<!-- gif1 bad di and glc doesn't work, gfi2 good di and glc works -->

Changing your launch angle also effects how far you're pushed back after being hit.

<!-- gif comparing how far you're pushed back just by changing DI -->

## Crouch Armor 

Condition 3 states that a GLC can only be preformed against moves that deal less than 80 knockback, but crouch armor can be used to increase that range. 

When your character is crouching, or is entering crouch, they gain crouch armor. It's applied on hit and decreases the knockback of a move by one-third, meaning a move that once dealt 120 knockback now deals 80. This means that if crouch armor is used, a GLC can be preformed against moves that deal less than 120 knockback. A GLC using crouch armor is called a CGLC (Crouching Grounded Land Cancel). 

Note that because crouch armor decreases knockback by one-third, it also increases the range at which Sakurai angles will launch at a horizontal angle, which makes it impossible to GLC. 

## Smash Charge Interrupt

If you are hit with a move while charging a smash attack, that move will deal 1.2 times more knockback, decreasing the range where a GLC can be preformed. 

\newpage 

# Application 

## Compound Diagonal ASDI/DI

If you gray stick GLC you'll control both ASDI and DI at the same time and compound their effects. 

The relative strength of ASDI down will change depending on a move's launch angle and the position of the gray stick. For example, lets look at what happens when DK tries to gray stick GLC Fox's strong, unstaled bair at 60%. 

| gray stick position | displacement | relative strength |
| :- | :- | :- |
| down| $2.228$ | $100\%$ | 
| down back| $1.512$ | $68\%$ | 
| down forward| $1.136$ | $51\%$ |

<!-- placeholder table -->

> $\text{Displacement} = \text{length of ASDI down } - \text{ initial vertical launch velocity}$


## SDI 

You can SDI during the hitlag of a move and still GLC if you ASDI down after. The amount and type of SDI you can get depends on whether you do a gray stick GLC, cstick GLC, gray stick CGLC, or cstick CGLC. 

### GLC

You're limited by what SDI is possible if you use gray stick for ASDI because the stick needs to end in the bottom half of the gate.

To get one SDI input during a gray stick GLC tap and hold down-forward or down-back. To get two SDI inputs during a gray stick GLC tap forward or back, then roll the stick down. Note that, because of compound diagonal ASDI/DI, the relative strength of ASDI down decreases if the gray stick is held on a diagonal. You can get around this in the one SDI method by tapping down-forward or down-back, then rolling the stick down. 

During a cstick GLC the gray stick doesn't need to end in the bottom half of the gate so the amount of SDI you can input is only limited by your speed---just make sure to not SDI up too much.

To get one SDI input during a cstick GLC tap forward or back. To get two SDI inputs during a cstick GLC tap forward or back and then roll the stick to down-forward or down-back. 

You can also tap forward or back twice if you're fast enough. Or, if you're really *really* fast, you can wank SDI if you want more than 2 SDI inputs. 

### CGLC

Crouch armor is applied on hit so you can SDI during the rest of hitlag with the only caveat being that you must start from a crouch.

Because you must start from a couch there is yet another restriction to preforming SDI during a gray stick CGLC. Not only do you have to end in the bottom half of the gate, but you have to start there too. The most consistent way to SDI during a gray stick CGLC is to hold down, then roll the stick to down-forward or down-back for 1 SDI input. Note that because of compound diagonal ASDI/DI the relative strength of ASDI down decreases if the gray stick is held on a diagonal. You could try to roll the stick back down after 1 SDI input to avoid it but it's a tricky input. 

A cstick CGLC has none of those restrictions. The gray stick is free to input as much SDI as you want as long as you start from a crouch. To get 1 SDI input hold down for crouch armor, then roll the stick to down-forward or down-back. To get 2 SDI inputs hold down for crouch armor, tap forward or back, then roll the stick to down-forward or down-back for quartercirlce SDI. 

## Buffered GLC

You can hold cstick down to buffer a GLC. 






















