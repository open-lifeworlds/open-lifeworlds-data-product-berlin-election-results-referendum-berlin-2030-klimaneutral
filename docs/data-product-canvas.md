
# Data Product Canvas - Berlin Election Results Referendum Berlin 2030 klimaneutral

## Metadata

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral
* license: CC-BY 4.0
* updated: 2025-03-18

## Input Ports

### Berlin LOR geodata

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/tree/main/data
* license: CC-BY-4.0
* updated: 2023-07-22

**Files**

* [berlin-lor-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts/berlin-lor-districts.geojson)
* [berlin-lor-forecast-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson)
* [berlin-lor-forecast-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson)
* [berlin-lor-district-regions-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson)
* [berlin-lor-district-regions-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson)
* [berlin-lor-planning-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson)
* [berlin-lor-planning-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson)

### Berlin Electoral Districts Berlin Election 2016

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-berlin-election-2016
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |

**Files**

* [berlin-electoral-districts-berlin-election-2016.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-berlin-election-2016/berlin-electoral-districts-berlin-election-2016.geojson)

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral
* license: GPLv3
* updated: 2025-03-17

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-districts.csv)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-electoral-districts.csv)

## Transformation Steps

* [Blender](../lib/transform/data_blender.py) blends data into geojson

## Output Ports

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson
* license: CC-BY 4.0
* updated: 2025-03-18

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics
* license: CC-BY 4.0
* updated: 2025-03-18

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-referendum-berlin-2030-klimaneutral/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json)

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

consumer-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).