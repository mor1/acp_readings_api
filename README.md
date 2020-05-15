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
`/api/historicaldata?date=&source=&sensor=&feature=` - Returns all the data for the given parameters.\
`/api/latestdata?source=&sensor=&feature=` - Returns the latest data for the given sensor and feature. If feature is not specified then returns the complete set of feature data.\