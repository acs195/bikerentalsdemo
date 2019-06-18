# bike rentals sketch
This is a sketch of a bike rental application.

## Design:
It consists of 4 main domain models: **Bike**, **RentalType**, **Promotion** and **Client** (we also have **BikeRental** and **PromotionRental**).

The **RentalType** defines the rent conditions (per hour, day or week) and price. When a client rents a bike, a **BikeRental** is added to the client's list of
rentals.

The **Promotion** (Family rental) establishes a discount under a criteria of min and max rentals.
When a client takes a promotion, chooses multiple **BikeRental** to be added to the client's list of promotions.

## Assumptions / comments:
  - I wrote only a few validations/exception cases.
  - The promotion proposed serves the purpose of applying a discount only when the condition of min and max rentals are met. Even though the values are dynamic, new methods are required to establish other criteria.
  - The logic for make the application interact with an user is not implemented.
  - I did not implement any persistent storage. I keep the lists within class variables.
  - The logging features implemented are very limited.

## Some best practices used:
  - PEP8 styling
  - Use of Docstrings
  - Automated unit Testing
  - No hardcoding
  - Modularity

---

## Set the environment before starting the application:
- Create virtual env:
  `virtualenv env`
- Activate virtual env:
  `source env/bin/activate`
- Install the required packages:
  `pip install -r requirements.txt`

## Testing:
`pytest -v --cov-report term-missing --cov-fail-under=85 --cov=. .`

## Run the application:
`python app/app.py`
