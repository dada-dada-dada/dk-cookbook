<!-- ---
title:  "Grab v0.1"
author: 'da'
...

\newpage -->

## Intro

For some ungodly reason DK's grab is the most complex move in the game. I have no idea what the developers were on when they made it. I'll try my best to go through everything as efficiently as I can, but don't expect any of it to make sense; we weren't meant to look behind this curtain. 

### Terminology 

| Term                   | definition                                                                                                                                         |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| grab escape            | when DK mashes out of a grab                                                                                                                       |
| grab release           | when DK releases an opponent from a normal grab                                                                                                    |
| cargo                  | the general cargo state                                                                                                                            |
| grounded cargo release | when DK releases an opponent from cargo on the ground                                                                                              |
| aerial cargo release   | when DK releases an opponent from cargo while in the air                                                                                           |
| port order             | port order from highest to lowest: 1, 2, 3, 4                                                                                                      |
| a / b                  | where a is the frame advantage or hitsun DK has if they have a higher port and b is the frame advantage or hitsun DK has if they have a lower port |

### Port Priority

DK's grab release will have one less frame of hitstun if his port is lower than the opponent's, meaning that he will have an extra frame of advantage. The differences can be seen in the in the table below. 

| animation     | higher Port | lower Port |
| :------------ | :---------- | :--------- |
| grab Release  | 30          | 29         |
| cargo Release | 15          | 14         |

All tests will be done with DK as the higher port unless otherwise specified. 

## Escape

DK has a unique property where he will experience 20 frames of hitstun instead of 30 if he escapes from a grab, meaning he will have a +9/+10 frame advantage over his opponent. There is enough time to safely dash away - and if the opponent is close enough - to counter attack. 

gif:https://thumbs.gfycat.com/BelatedHighHuia-size_restricted.gif

## Release

### Grip Strength

A counter called grip strength is created whenever you grab someone. As the opponent's percent increases so will your grip strength. The counter decreases as the opponent mashes, and they will break out when it reaches zero. Grab and cargo calculate grip strength and mashing differently so we'll look at each separately. 

#### Grab

The formula calculating a grab's initial grip strength can be described as the following:


![grip-strength](https://i.imgur.com/WboUh6z.png)

<!-- > Given the opponent's percent $p$, grab's initial grip strength $G(p)$ will be
> $$G(p) = \left\lfloor 40\left(\frac{p}{25}\right) + 75\right\rfloor$$ -->

The counter will naturally decay by 1 unit every frame until it reaches zero. If the opponent mashes they can decrease grip strength by an extra 12 units each frame (6 units for a stick input + 6 units for a button) for a maximum of 13 units per frame. 

gif:https://thumbs.gfycat.com/GloomyPassionateIraniangroundjay-size_restricted.gif,https://thumbs.gfycat.com/HugeFearfulAmericankestrel-size_restricted.gif

If the opponent mashes optimally, the formula calculating the minimum amount of frames required to mash out of a grab can be described as the following: 

![grab-mash](https://i.imgur.com/3lhQINi.png)

<!-- > Given the opponent's percent $p$, the minimum amount of frames required to mash out of grab will be 
> $$ M(p) = \left\lfloor \frac{G(p)}{13} \right\rfloor$$ -->

#### Grounded Cargo

The formula calculating cargo's initial grip strength can be described as the following: 

![cargo-gripstrength](https://i.imgur.com/B7m0dpu.png)

<!-- > Given the opponent's percent $p$, cargo's initial grip strength $C(p)$ will be 
> $$ C(p) = \left\lfloor 2 \left( \frac{p}{25}\right) + 14 \right\rfloor $$ -->

Grip strength will not decay while in cargo. The opponent can decrease grip strength by a maximum of 2 units each frame (1 unit for a stick input + 1 unit for a button). 

gif:https://thumbs.gfycat.com/SpanishDetailedFritillarybutterfly-size_restricted.gif,https://thumbs.gfycat.com/CavernousPracticalFirebelliedtoad-size_restricted.gif

If the opponent mashes optimally, the formula calculating the minimum amount of frames required to mash out of cargo can be described as the following: 

![groundedcargo-mash](https://i.imgur.com/GWMEbLX.png)

<!-- > Given the opponent's percent $p$, the minimum amount of frames required to mash out of grounded cargo will be 
> $$ N(p) = \left\lfloor \frac{C(p)}{2} \right\rfloor$$ -->

#### Aerial Cargo 

Melee handles mashing differently when DK is in aerial cargo. While the general rules for grounded cargo still apply, an extra unit of grip strength will be subtracted at random for each stick and button input, capping out at 3 units per frame. 

With this we can create a new optimal mashing formula: 

![aerialcargo-mash](https://i.imgur.com/VhcTTwT.png)

<!-- > Given the opponent's percent $p$, the minimum amount of frames required to mash out of aerial cargo will be
> $$ O(p) = \left\lfloor \frac{C(p)}{3} \right\rfloor $$ -->

gif:https://thumbs.gfycat.com/KnobbyOblongAngelwingmussel-size_restricted.gif,https://thumbs.gfycat.com/ForsakenAnxiousChrysalis-size_restricted.gif

#### Application

We can compare the two grip strength equations by graphing them on the same plane. 

![](https://i.imgur.com/ZmVzjHz.png)

While a grab's grip strength is always higher than a cargo's grip strength, each handle mashing differently. We can better understand this relationship by graphing the optimal mashing equations of grab and cargo on the same plane. 

![](https://i.imgur.com/Hn7sGWZ.png)

It's significantly easier to mash out of aerial cargo. If you need to move while in cargo, do as much of it as you can on the ground and throw as soon as possible in the air. 

### Grab Release

DK will be 0/+1 if he releases an opponent from grab, which is exactly the same as everyone else's grab release. It doesn't have any practical applications. 

### Cargo Release
#### Jumpkeeping

> Some information in this section was made by Optimism. 
> - [their twitter](https://twitter.com/ChampagneOpti)
> - [original smashboards post](https://smashboards.com/threads/jumpkeeping-a-new-dk-tech.481975/)

If DK cargos an opponent that has burned their second jump either by:

* air dodging
* double-jumping
* free-falling
* after or during upb and sideb

then releases them, they won't get their jump back. It's a niche option that sets up easy gimps and regrab shenanigans. 

gif:https://thumbs.gfycat.com/WhimsicalShallowArcticseal-size_restricted.gif,https://thumbs.gfycat.com/LeftFlashyArrowana-size_restricted.gif

#### Aerial Cargo Release

The amount of hitstun an opponent gets from a cargo release depends on their weight, and DK gets 14/15 frames of hitstun after they cargo release an opponent. The breakdown with the opponent's frame advantage is in the table below. 

> **DK P1, OPPONENT P2, AERIAL**
> 
> | character  | hitstun | opponent's advantage |
> | :--------- | :------ | :-------- |
> | bowser     | 15      | 0         |
> | dk         | 15      | 0         |
> | samus      | 15      | 0         |
> | ganon      | 15      | 0         |
> | yoshi      | 15      | 0         |
> | falcon     | 15      | 0         |
> | link       | 15      | 0         |
> | dr. mario  | 16      | -1        |
> | luigi      | 16      | -1        |
> | mario      | 16      | -1        |
> | ness       | 16      | -1        |
> | peach      | 16      | -1        |
> | shiek      | 16      | -1        |
> | zelda      | 16      | -1        |
> | icies      | 16      | -1        |
> | marth      | 16      | -1        |
> | mewtwo     | 16      | -1        |
> | roy        | 16      | -1        |
> | young link | 16      | -1        |
> | falco      | 17      | -2        |
> | pikachu    | 17      | -2        |
> | fox        | 17      | -2        |
> | kirby      | 17      | -2        |
> | jigglypuff | 18      | -3        |
> | g&w        | 18      | -3        |
> | pichu      | 18      | -3        |

It's not much, but the extra time widens your margin of error for gimps, and since DK's upb is active and invincible on frame 2 it's theoretically possible to stuff most escape option.

gif:https://thumbs.gfycat.com/FickleTinyCardinal-size_restricted.gif

#### Grounded Cargo Release

The numbers for initial hitstun are the same for grounded cargo release as aerial cargo release, but with a caveat; DK and the opponent pop into the air. 

gif:https://thumbs.gfycat.com/GraveEvilGrebe-size_restricted.gif
 
If the opponent lands on the ground they can cancel their initial hitstun with their landing lag. This can either decrease or increase their effective hitstun depending on their weight, ECB size, etc. The breakdown can be found in the table below. 

> Note: When DK does a grounded cargo release, he will land on the ground and have 15 frames of effective hitstun. 

> **DK P1, OPPONENT P2, GROUNDED, FLAT GROUND**
> 
> | character  | initial hitstun | effective hitstun | opponent's advantage | airborne after hitstun |
> | :--------- | :-------------- | :---------------- | :-------- | :--------------------- |
> | fox        | 17              | 9                 | +6        | no                     |
> | falco      | 17              | 11                | +4        | no                     |
> | ganon      | 15              | 13                | +2        | no                     |
> | bowser     | 15              | 14                | +1        | no                     |
> | falcon     | 15              | 15                | 0         | no                     |
> | dk         | 15              | 15                | 0         | no                     |
> | yoshi      | 15              | 15                | 0         | yes                    |
> | samus      | 15              | 15                | 0         | yes                    |
> | link       | 15              | 15                | 0        | yes                    |
> | sheik      | 16              | 16                | -1        | no                     |
> | young link | 16              | 16                | -1        | yes                    |
> | icies      | 16              | 16                | -1        | yes                    |
> | mario      | 16              | 16                | -1        | yes                    |
> | dr. mario  | 16              | 16                | -1        | yes                    |
> | ness       | 16              | 16                | -1        | yes                    |
> | marth      | 16              | 16                | -1        | yes                    |
> | mewtwo     | 16              | 16                | -1        | yes                    |
> | zelda      | 16              | 16                | -1        | yes                    |
> | peach      | 16              | 16                | -1        | yes                    |
> | luigi      | 16              | 16                | -1        | yes                    |
> | kirby      | 17              | 17                | -2        | yes                    |
> | pikachu    | 17              | 17                | -2        | yes                    |
> | roy        | 16              | 18                | -3        | no                     |
> | pichu      | 18              | 18                | -3        | yes                    |
> | g&w        | 18              | 18                | -3        | yes                    |
> | jigglypuff | 18              | 18                | -3        | yes                    |


Some characters are plus and can counter attack before DK's hitstun ends. 

gif:https://thumbs.gfycat.com/GreedyYellowishGrouse-size_restricted.gif

If the opponent times their mashing they can land on a platform and cancel most if not all their initial hitstun.

gif:https://thumbs.gfycat.com/CraftyCloudyBluegill-size_restricted.gif

Some characters are still airborne after their initial hitstun ends which can severely restricts their options. They either have to jump and risk being juggled or attack and risk getting CC'd. 

gif:https://thumbs.gfycat.com/TightRemoteDrongo-size_restricted.gif,https://thumbs.gfycat.com/UncommonForsakenHorse-size_restricted.gif

gif:https://thumbs.gfycat.com/ClutteredAjarCarpenterant-size_restricted.gif

This can be combined with jumpkeeping to further restrict the opponent's options. Some characters like Marth only have time to jump after their initial hitstun ends, but if they can't jump, they're forced to land and receive even more hitstun. More character specific labbing needs to be done. 