# Introduction
Create an online home delivery service for one of the most successful Wok restaurant chains, E-wok.

One of the most successful Wok restaurant chains is preparing the launch of the online home delivery service. To do this, a special selection of Woks has been created that will be put up for sale on its new E-wok service.

Its online launch plan is divided into different phases, in order to make it known to customers as soon as possible. We have been asked to develop this service in 5 steps.

## Step 1 - E-wok menu

In this first step, customers can start consulting the E-wok menu.

To do this, we will create a CLI application that will simply display the available woks. Response example:

- E-wok menu:
  (1) Wok Wokling - small size (noodles, calamari, shitake, sweet and sour sauce) - 4 €
  (2) Wok Wicket (noodles, beef, bacon, green beans, hot sauce) - 6 €
  (3) Wok Endor (rice, chicken breast, red and green pepper, curry sauce)  - 7 €
  (4) Wok Kneesaa (rice, broccoli, mushrooms, corn, yakisoba sauce) - 6 €

No user interaction required.

## Step 2 - Order your E-wok

In this second step, customers can now place their order in E-wok.

To be able to place the order, we will extend the CLI application from Step 1 with the following functionalities:

    Choose a wok from the menu (showing the menu from 1 to 4)

    Choose quantity (maximum 5 units)

    Show total to pay

Example:

- E-wok menu:
  (1) Wok Wokling - small size (noodles, calamari, shitake, sweet and sour sauce) - 4 €
  (2) Wok Wicket (noodles, beef, bacon, green beans, hot sauce) - 6 €
  (3) Wok Endor (rice, chicken breast, red and green pepper, curry sauce)  - 7 €
  (4) Wok Kneesaa (rice, broccoli, mushrooms, corn, yakisoba sauce) - 6 €
- Choose a wok from the menu (1 to 4): 2
- Choose quantity (1 to 5): 2
- Total to pay: 12 €

## Step 3 - Customize your E-wok order

In this third step, customers can customize their order with their name and add an extra ingredient to the selected wok.

We will extend the CLI application from Step 2, adding two functionalities:

    Enter customer name

    Add extra ingredient 1€ extra (1 - Cherry tomato, 2 - Prawns, 3 - Pineapple)

Example:

- Your name: Rviewer
- E-wok menu:
  (1) Wok Wokling - small size (noodles, calamari, shitake, sweet and sour sauce) - 4 €
  (2) Wok Wicket (noodles, beef, bacon, green beans, hot sauce) - 6 €
  (3) Wok Endor (rice, chicken breast, red and green pepper, curry sauce)  - 7 €
  (4) Wok Kneesaa (rice, broccoli, mushrooms, corn, yakisoba sauce) - 6 €
- Choose a wok from the menu (1 to 4): 2
- Choose quantity (1 to 5): 2
- Choose an extra ingredient for 1€ [(0) - None, (1) - Cherry tomato, (2) - Prawns, 3 - Pineapple]: 3
- Total to pay: 13 €

## Step 4 - E-wok order inventory

To facilitate the work of the E-wok cooks, it will be necessary to save and obtain a list of all the orders that are requested via the CLI application. To do this, they ask us to create an API.

From this step, we are going to save the orders made to us through the CLI application from the previous steps. You can choose the storage method you prefer. From these saved orders, we will provide data to our API.

E-Wok API will have two endpoints:

    List all orders

    List all the orders for a customer name

To develop the API, they provide us with a definition file.

## Step 5 - E-wok discounts

To retain customers who place more orders at E-wok, a series of discounts will be added to the CLI application.

    10% discount from the 2nd order (included) of the same customer

    20% discount from the 4th order (included) of the same customer

    The discounts are not cumulative, the discount of the corresponding section will be applied.

    The discount will be applied after showing the total to pay.

Example:

- Total to pay: 13 €
- Total to pay with 10% discount (3rd order): 11.7 €
