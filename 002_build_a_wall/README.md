# Introduction
Create the strongest wall of all time! Combine bricks and avoid instability!

Most of us were playing with Lego (or even better, Tente) when we were children, and we know how complex is to build something strong that doesn't fall down when you have to add something heavy above, right?

We had discovered, after many times and frustration, that the bricks for any wall have to be well-placed among each others to achieve a really strong wall.

So, the aim of this Challenge is to create the strongest wall of all time! You will have to combine bricks, in a proper way, to avoid instability.

# How it works?

This is a CLI application that receives 2 arguments and represent the created wall in ASCII, easy-peasy, isn't it? Well, let's see...

To do so, your CLI command have to receive the following parameters:

    Number of rows: The number of rows of bricks the wall has to have

    Number of bricks: The number of bricks you have to use on each row to represent the wall.

# Constraints
## How to represent your wall

To represent your one-and-only creation you have to use the following elements:

    ■■: A full brick (2 of ■). The bigger brick for the wall

    ■: Half a brick. The smallest unit

    |: Mortar. The cement between each brick on the same row

## How to build a strong wall

Any builder knows that, if you just put a brick over another, your wall is going to fall down as you turn your back!

To build a strong wall you have to follow these considerations:

    There has to be a mortar (|) every brick (half or full) on the same row

    Bricks cannot be aligned vertically with the bricks of the row above or below it, to provide more stability

## Constraints

    If one or both of the arguments aren't valid (less than 1 brick, isn't integer, not present, ...etc) return null.

    If the number of bricks required to build the wall is greater than 10.000 return Naah, too much...here's my resignation.

# Examples

Here you could see some examples of the expected output:
<pre><code>$> build 5 5
     ■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■

$> build 10 7
     ■|■■|■■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■|■■|■■
     ■|■■|■■|■■|■■|■■|■■|■
     ■■|■■|■■|■■|■■|■■|■■

$> build "eight" [3]
    null
    
$> build 12 -4
    null
    
$> build 123 1024
    Naah, too much...here's my resignation.
</pre></code>

https://rviewer.io/app/developers/challenge-library?frameworks=&languages=