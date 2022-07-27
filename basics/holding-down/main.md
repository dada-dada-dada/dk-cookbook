---
title: "The Mechanics Of Crouch Cancelling"
---


\newpage

There are so many different terms that are thrown around when people talk about crouch cancel. They're awful and don't do a good job describing what's actually happening on a mechanical level. Like, you can crouch cancel, but to do it you don't have to crouch, and if you do crouch it doesn't automatically mean you'll cancel your lag, but if you crouch and cancel your lag then it's a "true" crouch cancel. It's dumb. 

For the sake of this guide we'll get rid of them all and work with a couple new terms: land cancel (LC) and grounded land cancel (GLC).

# Land Cancels

If you are hit with a move in the air and are not in tumble you can land on the ground and cancel the rest of your hitstun with your landing animation. 

gif:https://gfycat.com/acrobaticglassdeermouse,https://gfycat.com/secondhandrecentlemming

The length of the landing animation varies from character to character, but the average is around 4 frames with a couple outliers shown here:  

| Character | Length in Frames |
| :-    | :- | 
| Pichu | 2 |
| DK | 5 |
| Ganon | 5 |
| Bowser | 6 |
| Everyone Else | 4 |

<!-- - [Clip 1](https://gfycat.com/acrobaticglassdeermouse) 
- [Clip 2](https://gfycat.com/secondhandrecentlemming) -->

It's uses are endless, but that's not the point of this guide. We're interested in its variation: the grounded land cancel. 

The general idea behind a GLC is the same as an LC. The difference is that you use quirks of the physics engine to do it from the ground. The following conditions must be met to preform a GLC: 

1. the distance you ASDI down is greater than the distance you're launched up
2. you're hit with a move with an upwards launch angle
3. you're hit with a move that deals less than 80 knockback

## Condition 1

A GLC is built on the fact that some moves launch you into the air, and you can use ASDI to teleport back down to cancel whatever hitstun you had with an LC. The game takes the vector of your launch velocity, adds the vector of your ASDI, and then uses that as your new position. All this happens in one frame. It only works as long as the distance you're launched up is less than the distance you teleport back down. For reference, ASDI straight down moves your character by three in-game units. 

gif:https://gfycat.com/powerfulnaturalfirebelliedtoad,https://gfycat.com/jaggedpalatableanteater

<!-- - [Clip 1](https://gfycat.com/powerfulnaturalfirebelliedtoad) 
- [Clip 2](https://gfycat.com/jaggedpalatableanteater) -->

SDI can't be used to teleport back down. You can only SDI during hitlag and therefore it can't interact with your launch velocity, so no matter how much you try to SDI down your environmental collision box will collide with the floor and the game will place you back on top.

gif:https://gfycat.com/personaltangiblehackee

<!-- - [Clip 1](https://gfycat.com/personaltangiblehackee) -->

## Condition 2

If you are on the ground and are not hit at an upwards angle it is impossible to ASDI or SDI vertically, making it impossible to GLC. This was a conscious design choice by the developers because they realized that, hey, all the meteors we spent so much time programming don't work if you just hold up.

gif:https://gfycat.com/focusedknobbyfinch

<!-- - [Clip 1](https://gfycat.com/focusedknobbyfinch) -->

Other edge cases are moves that have a Sakurai angle. If a move has a Sakurai angle, the angle it launches at will change depending on position and knockback dealt. 

![](https://i.imgur.com/XTvOy80.png)

If a grounded character is hit with a move that has a Sakurai angle and it deals a maximum of 32 knockback, they'll be launched at a horizontal angle, which makes it impossible to GLC. 

gif:https://gfycat.com/preciousagedfanworms,https://gfycat.com/calculatingearlyhadrosaurus

<!-- - [Clip 1](https://gfycat.com/preciousagedfanworms)
- [Clip 2](https://gfycat.com/calculatingearlyhadrosaurus) -->


You can still LC a move without an upwards trajectory if you start in the air. 

gif:https://gfycat.com/personalspiritedhoiho

<!-- - [Clip 1](https://gfycat.com/personalspiritedhoiho) -->
  
## Condition 3

When someone is launched into the air they can enter either non-tumble or tumble hitstun. If you hit the ground during non-tumble you'll land normally and preform and LC, but if you hit the ground while in tumble you'll be knocked down. A character enters tumble when they're hit with a move that deals at least 80 knockback. Therefore, a GLC can only be preformed against moves that deal less than 80 knockback.

gif:https://gfycat.com/necessaryweirdhadrosaurus,https://gfycat.com/advancedblissfuladdax

<!-- - [Clip 1](https://gfycat.com/necessaryweirdhadrosaurus)
- [Clip 2](https://gfycat.com/advancedblissfuladdax) -->

Crossing the knockback threshold is the main bottleneck for preforming a GLC. You'll almost always pass over the 80 knockback mark before your initial vertical launch velocity is greater than the distance you ASDI down. It's the reason why you can still Amsah tech strong moves at high percents. 

# Other Variables 

## Gray Stick and CStick ASDI 

You can input ASDI with the gray stick or the cstick. While they're functionally identical, which you choose will significantly impact what you can do during and after a GLC. While the gray stick is more convenient, you have to control your ASDI, crouch armor, SDI, DI, and movement with just one input device, but if you use the cstick that burden is spread across two input devices. 

If you use the gray stick for ASDI it's called a gray stick GLC. If you use the cstick for ASDI it's called a cstick GLC. The distinction is useful when describing the technical aspects of a GLC. The normal notation is fine for most usecases; I just want to be thourough. 

## Diagonal ASDI

Melee is an analogue game. You don't have to hold all the way down on the gray stick or cstick to preform a GLC. The only thing that matters is that the distance you travel down with ASDI down is greater than the distance you travel up from your vertical launch velocity. That extra leeway can be used to do diagonal ASDI.

Diagonal ASDI can change how far you travel horizontally during a GLC. 

gif:https://gfycat.com/talkativegrizzledindianpangolin

<!-- - [Clip 1](https://gfycat.com/talkativegrizzledindianpangolin) -->

You can use that extra boost to fight back against a move's pushback or to escape pressure. 

gif:https://gfycat.com/selfreliantthoroughbactrian,https://gfycat.com/greatscaryamericanbobtail

<!-- - [Clip 1](https://gfycat.com/selfreliantthoroughbactrian)
- [Clip 2](https://gfycat.com/greatscaryamericanbobtail) -->

## DI

DI changes your launch angle, and when your launch angle changes so does your launch velocity, meaning that depending on how you DI a move you'll either decrease or increase the distance needed to ASDI down. 

![](https://i.imgur.com/6naooeE.png)

Changing your launch angle also effects how far you're pushed back after being hit.

gif:https://gfycat.com/wigglyreasonablechrysalis

<!-- - [Clip 1](https://gfycat.com/wigglyreasonablechrysalis) -->

## Crouch Armor 

Condition 3 states that a GLC can only be preformed against moves that deal less than 80 knockback, but crouch armor can be used to increase that range. 

When your character is crouching, or is entering crouch, they gain crouch armor. It's applied on hit and decreases the knockback of a move by one-third, meaning a move that once dealt 120 knockback now deals 80. This means that if crouch armor is used, a GLC can be preformed against moves that deal less than 120 knockback. A GLC using crouch armor is called a CGLC (Crouching Grounded Land Cancel). 

gif:https://gfycat.com/prestigiousdesertedballoonfish,https://gfycat.com/palecelebratedbagworm

<!-- - [Clip 1](https://gfycat.com/prestigiousdesertedballoonfish)
- [Clip 2](https://gfycat.com/palecelebratedbagworm) -->

Note that because crouch armor decreases knockback by one-third, it also increases the range at which Sakurai angles will launch at a horizontal angle, which makes it impossible to GLC. 

## Smash Charge Interrupt

If you are hit with a move while charging a smash attack that move will deal 1.2 times more knockback, meaning a GLC can only be preform against moves that deal less than 67 knockback. 

gif:https://gfycat.com/slimyelementaryaxisdeer,https://gfycat.com/detailedpossiblechrysomelid

## SDI

You can SDI during the hitlag of a move and still GLC if you ASDI down. 

gif:https://gfycat.com/meaneminenthydra

The amount and type of SDI you can get depends on the method used to GLC. To SDI during a gray stick GLC you can: 

- Start at down, then roll the stick to down-forward / down-back
- Start at forward / back, then roll the stick to down-forward / down-back

> Note: the latter method is less consistent than the former because the stick needs to end in the bottom half of the gate to get the correct ASDI. If you fail, so does your GLC. 

To SDI during a gray stick CGLC you can: 

- start at down, then roll the stick to down-forward / down-back

To SDI during a cstick GLC you can:

- tap forward / back 
- tap forward / back, then roll the stick to down-forward / down-back

> Note: it's significantly easier to do 2 SDI inputs during a cstick GLC compared to a gray stick GLC because the stick doesn't need to end in the bottom half of the gate. If you fail to get 2 SDI you'll still GLC. 

To SDI during a cstick CGLC you can: 

- start at down, then roll the stick to down-forward / down-back
- start at down, then tap forward / back

# Application

## Buffered GLC

You can automatically preform a GLC if you buffer cstick down during another action. It's most commonly buffered during an initial dash, but it can be done during any type of lag. 

gif:https://gfycat.com/flusteredaltruisticbabirusa

The gray stick is free to move as normal, but be careful to not accidentally SDI up or you'll be launched too high for a GLC to work. The cstick can also be held at an angle to get the benefits of diagonal ASDI.

### Survival GLC

On top of buffering ASDI you can also buffer DI. 

If you lock out tap jump by buffering up during lag you can do a GLC with survival DI, also known as a survival GLC. It's incredibly strong. By literally decreasing your horizontal launch velocity a survival GLC can practically remove pushback. Moves that were once impossible to punish are now in reach, and the effect can be futher amplified with diagonal ASDI.

gif:https://gfycat.com/altruisticaccuratehound

While you don't have the same freedom of movement as a normal buffered GLC, you can still walk while buffering a survival GLC. Character's like Sheik become a moving landmine, tanking hits while still being able to uTilt and fTilt. It's also possible buffer a survival GLC during the lag of an approaching move or wavedash. This is useful for characters that have good grounded burst options, like the Ice Climbers. 

gif:https://gfycat.com/frayedbravearmednylonshrimp,https://gfycat.com/sanebewitchedasiantrumpetfish

> The savestates used in this clip were provided by Nopia. Thanks!

A side effect of reducing your horizontal launch velocity is that the effect of momentum stacking will decrease significantly. Dashes out of a GLC should be a near-max speed. 

gif:https://gfycat.com/nextuntimelybighorn

> This clip is using Marth's wavedash back for clarity's sake. 

Unfortunately it's impossible for a human to survival CGLC because, as you move the stick from the bottom half of the gate to the top half, you will SDI up and will be too high for ADSI to bring you back down. 

### Combo GLC

If you hold down-back you can buffer a GLC with combo DI, also known as a combo GLC. By inreasing your horizontal launch velocity a combo GLC increases pushback, allowing you to remain actionable while escaping pressure.

gif:https://gfycat.com/opulentabsolutefennecfox

gif:https://gfycat.com/easyunconsciousfantail,https://gfycat.com/unsteadyimportantflies

Naturally, a combo CGLC is also possible, and since you don't need to worry about locking out tap jump you can also SDI.

gif:https://gfycat.com/practicalslimhackee