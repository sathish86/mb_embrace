import pytest
from embrace_app import utils
import json

data = """
[
  {
    "$distance": 526.0582,
    "address": "151 Hawkesbury Rd",
    "category_ids": [
      342,
      347
    ],
    "category_labels": [
      [
        "Social",
        "Food and Dining",
        "Cafes, Coffee and Tea Houses"
      ],
      [
        "Social",
        "Food and Dining",
        "Restaurants"
      ]
    ],
    "country": "au",
    "cuisine": [
      "Coffee",
      "Cafe"
    ],
    "factual_id": "2b2fdb2f-b044-452f-8241-7be2a7bcae4a",
    "latitude": -33.807325,
    "locality": "Westmead",
    "longitude": 150.987654,
    "name": "Mrs Meads Coffee Shop",
    "neighborhood": [
      "Westmead"
    ],
    "postcode": "2145",
    "region": "NSW",
    "tel": "(02) 9689 3880"
  },
  {
    "$distance": 573.1589,
    "accessible_wheelchair": true,
    "address": "151-155 Hawkesbury Rd",
    "address_extended": "Shop 6",
    "category_ids": [
      342,
      355
    ],
    "category_labels": [
      [
        "Social",
        "Food and Dining",
        "Cafes, Coffee and Tea Houses"
      ],
      [
        "Social",
        "Food and Dining",
        "Restaurants",
        "Fast Food"
      ]
    ],
    "country": "au",
    "cuisine": [
      "Cafe",
      "Australian",
      "Burgers",
      "Coffee",
      "Italian"
    ],
    "factual_id": "24734648-f96a-4717-b5a5-b8ad23a57c58",
    "fax": "(02) 9689 3558",
    "hours": {
      "friday": [
        [
          "7:00",
          "16:00"
        ]
      ],
      "monday": [
        [
          "7:00",
          "16:00"
        ]
      ],
      "thursday": [
        [
          "7:00",
          "16:00"
        ]
      ],
      "tuesday": [
        [
          "7:00",
          "16:00"
        ]
      ],
      "wednesday": [
        [
          "7:00",
          "16:00"
        ]
      ]
    },
    "hours_display": "Mon-Fri 7:00-16:00",
    "kids_goodfor": true,
    "latitude": -33.807003,
    "locality": "Westmead",
    "longitude": 150.988087,
    "meal_breakfast": true,
    "meal_cater": true,
    "meal_deliver": false,
    "meal_dinner": true,
    "meal_lunch": true,
    "meal_takeout": true,
    "name": "Sit 'n' Chats Cafe",
    "neighborhood": [
      "Westmead"
    ],
    "open_24hrs": false,
    "options_glutenfree": true,
    "options_healthy": true,
    "options_vegan": true,
    "options_vegetarian": true,
    "parking": true,
    "payment_cashonly": false,
    "postcode": "2145",
    "price": 2,
    "region": "NSW",
    "reservations": true,
    "seating_outdoor": true,
    "tel": "(02) 9689 3880"
  },
  {
    "$distance": 1001.475,
    "accessible_wheelchair": true,
    "address": "42 Dunmore St",
    "address_extended": "Shop 1",
    "alcohol": true,
    "category_ids": [
      342,
      347
    ],
    "category_labels": [
      [
        "Social",
        "Food and Dining",
        "Cafes, Coffee and Tea Houses"
      ],
      [
        "Social",
        "Food and Dining",
        "Restaurants"
      ]
    ],
    "country": "au",
    "cuisine": [
      "Cafe",
      "Coffee",
      "Burgers"
    ],
    "factual_id": "f1a2e366-86cd-4e18-b198-adaf9515bbab",
    "hours": {
      "friday": [
        [
          "7:30",
          "15:30"
        ]
      ],
      "monday": [
        [
          "7:30",
          "15:30"
        ]
      ],
      "saturday": [
        [
          "7:30",
          "15:30"
        ]
      ],
      "thursday": [
        [
          "7:30",
          "15:30"
        ]
      ],
      "tuesday": [
        [
          "7:30",
          "15:30"
        ]
      ],
      "wednesday": [
        [
          "7:30",
          "15:30"
        ]
      ]
    },
    "hours_display": "Mon-Sat 7:30-15:30",
    "latitude": -33.807827,
    "locality": "Wentworthville",
    "longitude": 150.971255,
    "meal_breakfast": true,
    "meal_cater": false,
    "meal_deliver": false,
    "meal_lunch": true,
    "meal_takeout": true,
    "name": "Sunny Spot Cafe",
    "open_24hrs": false,
    "payment_cashonly": false,
    "postcode": "2145",
    "price": 2,
    "region": "NSW",
    "seating_outdoor": true,
    "tel": "(02) 9631 3224"
  },
  {
    "$distance": 1063.7375,
    "address": "The Children's Hospital at Westmead",
    "category_ids": [
      342
    ],
    "category_labels": [
      [
        "Social",
        "Food and Dining",
        "Cafes, Coffee and Tea Houses"
      ]
    ],
    "country": "au",
    "cuisine": [
      "Coffee",
      "Cafe"
    ],
    "factual_id": "0c52f513-3948-47d6-8e8c-d36285ec084b",
    "hours": {
      "friday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "monday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "saturday": [
        [
          "7:00",
          "22:00"
        ]
      ],
      "sunday": [
        [
          "7:30",
          "22:00"
        ]
      ],
      "thursday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "tuesday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "wednesday": [
        [
          "6:00",
          "23:00"
        ]
      ]
    },
    "hours_display": "Mon-Fri 6:00-23:00; Sat 7:00-22:00; Sun 7:30-22:00",
    "latitude": -33.803476,
    "locality": "Westmead",
    "longitude": 150.992029,
    "name": "Starbucks",
    "neighborhood": [
      "Westmead",
      "Northmead"
    ],
    "open_24hrs": false,
    "postcode": "2145",
    "region": "NSW",
    "tel": "(02) 9687 4991",
    "website": "http://www.starbucks.com.au/Home.php"
  },
  {
    "$distance": 1192.3525,
    "address": "Cnr Hawkesbury Rd & Hainsworth St",
    "address_extended": "Level 2",
    "attire": "casual",
    "category_ids": [
      342
    ],
    "category_labels": [
      [
        "Social",
        "Food and Dining",
        "Cafes, Coffee and Tea Houses"
      ]
    ],
    "country": "au",
    "cuisine": [
      "Coffee",
      "Australian",
      "Cafe"
    ],
    "factual_id": "cb258ff6-fba8-4050-9424-6439efc4d8e2",
    "hours": {
      "friday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "monday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "saturday": [
        [
          "7:00",
          "22:00"
        ]
      ],
      "sunday": [
        [
          "7:30",
          "22:00"
        ]
      ],
      "thursday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "tuesday": [
        [
          "6:00",
          "23:00"
        ]
      ],
      "wednesday": [
        [
          "6:00",
          "23:00"
        ]
      ]
    },
    "hours_display": "Mon-Fri 6:00-23:00; Sat 7:00-22:00; Sun 7:30-22:00",
    "latitude": -33.802568,
    "locality": "Westmead",
    "longitude": 150.992994,
    "meal_breakfast": true,
    "meal_cater": false,
    "meal_deliver": false,
    "meal_lunch": true,
    "meal_takeout": true,
    "name": "Starbucks",
    "neighborhood": [
      "Westmead"
    ],
    "open_24hrs": false,
    "options_healthy": true,
    "options_vegetarian": true,
    "payment_cashonly": false,
    "postcode": "2145",
    "price": 2,
    "rating": 3.5,
    "region": "NSW",
    "reservations": false,
    "tel": "(02) 9687 4991",
    "website": "http://www.starbucks.com.au/Home.php"
  }
]"""


class TestUtils(object):

    def test_utils__remove_unwanted_data(self):
        """
        check it removes unwanted field from data
        :return:
        """
        temp_data = json.loads(data)
        result_data = utils.filter_output(temp_data)
        for rec in result_data:
            assert "category_ids" in rec
            assert "factual_id" in rec