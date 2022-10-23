from dataclasses import dataclass


@dataclass(kw_only=True)
class Agency:
    agency_id: str = None
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_lang: str = None
    agency_phone: str = None
    agency_fare_url: str = None
    agency_email: str = None


@dataclass(kw_only=True)
class Stops:
    stop_id: str
    stop_code: str = None
    stop_name: str = None
    stop_desc: str = None
    stop_lat: float = None
    stop_lon: float = None
    zone_id: str = None
    stop_url: str = None
    location_type: int = None
    parent_station: str = None
    stop_timezone: str = None
    wheelchair_boarding: int = None
    level_id: str = None
    platform_code: str = None


@dataclass(kw_only=True)
class Routes:
    route_id: str
    agency_id: str = None
    route_short_name: str = None
    route_long_name: str = None
    route_desc: str = None
    route_type: int
    route_url: str = None
    route_color: str = None
    route_text_color: str = None
    route_sort_order: int = None
    continuous_pickup: int = None
    continuous_drop_off: int = None


@dataclass(kw_only=True)
class Trips:
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str = None
    trip_short_name: str = None
    direction_id: int = None
    block_id: str = None
    shape_id: str = None
    wheelchair_accessible: int = None
    bikes_allowed: int = None


@dataclass(kw_only=True)
class StopTimes:
    trip_id: str
    arrival_time: int = None
    departure_time: int = None
    stop_id: str
    stop_sequence: int
    stop_headsign: str = None
    pickup_type: int = None
    drop_off_type: int = None
    continuous_pickup: int = None
    continuous_drop_off: int = None
    shape_dist_traveled: float = None
    timepoint: int = None


@dataclass(kw_only=True)
class Calendar:
    service_id: str
    monday: int
    tuesday: int
    wednesday: int
    thursday: int
    friday: int
    saturday: int
    sunday: int
    start_date: int
    end_date: int


@dataclass(kw_only=True)
class CalendarDates:
    service_id: str
    date: int
    exception_type: int


@dataclass(kw_only=True)
class FareAttributes:
    fare_id: str
    price: float
    currency_type: str
    payment_method: int
    transfers: int
    agency_id: str = None
    transfer_duration: int = None


@dataclass(kw_only=True)
class FareRules:
    fare_id: str
    route_id: str = None
    origin_id: str = None
    destination_id: str = None
    contains_id: str = None


@dataclass(kw_only=True)
class Shapes:
    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: int
    shape_dist_traveled: float = None


@dataclass(kw_only=True)
class Frequencies:
    trip_id: str
    start_time: int
    end_time: int
    headway_secs: int
    exact_times: int = None


@dataclass(kw_only=True)
class Transfers:
    from_stop_id: str
    to_stop_id: str
    transfer_type: int
    min_transfer_time: int = None


@dataclass(kw_only=True)
class Pathways:
    pathway_id: str
    from_stop_id: str
    to_stop_id: str
    pathway_mode: int
    is_bidirectional: int
    length: float = None
    traversal_time: str = None
    stair_count: str = None
    max_slope: str = None
    min_width: str = None
    signposted_as: str = None
    reversed_signposted_as: str = None


@dataclass(kw_only=True)
class Levels:
    level_id: str
    level_index: str
    level_name: str = None


@dataclass(kw_only=True)
class FeedInfo:
    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: str
    default_lang: str = None
    feed_start_date: int = None
    feed_end_date: int = None
    feed_version: str = None
    feed_contact_email: str = None
    feed_contact_url: str = None


@dataclass(kw_only=True)
class Translations:
    table_name: str
    field_name: str
    language: str
    translation: str
    record_id: str = None
    record_sub_id: str = None
    field_value: str = None


@dataclass(kw_only=True)
class Attributions:
    attribution_id: str = None
    agency_id: str = None
    route_id: str = None
    trip_id: str = None
    organization_name: str
    is_producer: int = None
    is_operator: int = None
    is_authority: int = None
    attribution_url: str = None
    attribution_email: str = None
    attribution_phone: str = None
