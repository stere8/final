from enum import Enum

class ListingStatus(Enum):
    ACTIVE = "Active"
    PENDING = "Pending"
    SOLD = "Sold"

class OrderStatus(Enum):
    PENDING = "Pending"
    FINISHED = "Finished"
    CANCELED = "Canceled"