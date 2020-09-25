from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Wohnung(object):
    image_url: str
    name: str
    address: str
    price: str
    detail_url: str
