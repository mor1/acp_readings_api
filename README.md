# Adaptive City Program Time Data Reading API (Work in Progress)

This project provides a set of restful APIs allowing access to the sensor data on the Adaptive City Platform.

## Getting Started

### Prerequisites

Before you run the API server, be sure you have these downloaded/installed on your machine:

+ Python3
+ python-flask (use python-pip)

### Installing

Navigate inside the root folder and run,

```
python acp_readings_api.py
```

This will start the server on the port specified in the file. Default is 8001. The API endpoints could be accessed by querying *http://localhost:8001/endpoint*

#### API References
1. `/api/readings/historicaldata?date=&source=&sensor=&feature=` - Returns all the data for the given parameters.\
2. `/api/readings/latestdata?source=&sensor=&feature=` - Returns the latest data for the given sensor and feature. If feature is not specified then returns the complete set of feature data. Sample Output:
    + `/api/readings/latestdata?source=mqtt_ttn&sensor=elsys-co2-0461e3`: {"features": {"co2": 415, "device": "elsys_co2", "humidity": 36, "light": 0, "motion": 2, "temperature": 15.3, "vdd": 3659}}
    + `/api/readings/latestdata?source=mqtt_ttn&sensor=elsys-co2-0461e3&feature=co2`: {"co2": 415}