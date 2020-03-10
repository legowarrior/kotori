# -*- coding: utf-8 -*-
# (c) 2020 Andreas Motl <andreas@getkotori.org>
import logging
import pytest_twisted

from test.resources import influx, mqtt_topic, PROCESS_DELAY
from test.util import mqtt_sensor, sleep

logger = logging.getLogger(__name__)


@pytest_twisted.inlineCallbacks
def test_timestamp_rfc3339(machinery, create_influxdb, reset_influxdb):

    # Submit a single measurement, with timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
        'timestamp': '2020-03-10 03:38:37.937059000+01:00'
    }
    yield mqtt_sensor(mqtt_topic, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)

    # Proof that data arrived in InfluxDB.
    record = influx.get_first_record()
    assert record == {u'time': u'2020-03-10T02:38:37.937058816Z', u'humidity': 83.1, u'temperature': 42.84}
    yield record


@pytest_twisted.inlineCallbacks
def test_timestamp_seconds(machinery, create_influxdb, reset_influxdb):

    # Submit a single measurement, with timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
        'timestamp': 1583810982
    }
    yield mqtt_sensor(mqtt_topic, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)

    # Proof that data arrived in InfluxDB.
    record = influx.get_first_record()
    assert record == {u'time': u'2020-03-10T03:29:42Z', u'humidity': 83.1, u'temperature': 42.84}
    yield record


@pytest_twisted.inlineCallbacks
def test_timestamp_milliseconds(machinery, create_influxdb, reset_influxdb):

    # Submit a single measurement, with timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
        'timestamp': 1583810982123
    }
    yield mqtt_sensor(mqtt_topic, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)

    # Proof that data arrived in InfluxDB.
    record = influx.get_first_record()
    assert record == {u'time': u'2020-03-10T03:29:42.123Z', u'humidity': 83.1, u'temperature': 42.84}
    yield record


@pytest_twisted.inlineCallbacks
def test_timestamp_microseconds(machinery, create_influxdb, reset_influxdb):

    # Submit a single measurement, with timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
        'timestamp': 1583810982123456
    }
    yield mqtt_sensor(mqtt_topic, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)

    # Proof that data arrived in InfluxDB.
    record = influx.get_first_record()
    assert record == {u'time': u'2020-03-10T03:29:42.123456Z', u'humidity': 83.1, u'temperature': 42.84}
    yield record


@pytest_twisted.inlineCallbacks
def test_timestamp_nanoseconds(machinery, create_influxdb, reset_influxdb):

    # Submit a single measurement, with timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
        'timestamp': 1583810982123456789
    }
    yield mqtt_sensor(mqtt_topic, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)

    # Proof that data arrived in InfluxDB.
    record = influx.get_first_record()
    assert record == {u'time': u'2020-03-10T03:29:42.123456768Z', u'humidity': 83.1, u'temperature': 42.84}
    yield record