import json
import os
import re
import warnings

import pandas as pd

from lib.tracking_decorator import TrackingDecorator

warnings.filterwarnings("ignore", category=UserWarning)


@TrackingDecorator.track_time
def blend_data(
    data_product_manifest,
    data_transformation,
    source_path,
    results_path,
    clean=False,
    quiet=False,
):
    already_exists, converted, exception = 0, 0, 0

    for input_port in data_transformation.input_ports or []:
        # Initialize statistics
        json_statistics = {}

        statistics_file_path = os.path.join(
            results_path,
            f"{input_port.id}-statistics",
            f"{input_port.id}-statistics.json",
        )

        year = re.search(r"\b\d{4}\b", input_port.id).group()
        half_year = (
            re.search(r"\b\d{2}(?<!\d{4})\b", input_port.id).group()
            if re.search(r"\b\d{2}(?<!\d{4})\b", input_port.id)
            else "00"
        )

        # Build statistics structure
        if year not in json_statistics:
            json_statistics[year] = {}
        if half_year not in json_statistics[year]:
            json_statistics[year][half_year] = {}

        for file in input_port.files or []:
            source_file_path = os.path.join(
                source_path, input_port.id, file.source_file_name
            )
            target_file_path = os.path.join(
                results_path,
                f"{input_port.id}-geojson",
                f"{input_port.id}-{year}-{half_year}-{file.area_type}.geojson",
            )
            geojson_template_file_path = os.path.join(
                source_path, file.geojson_template_file_name
            )

            try:
                # Load geojson
                with open(
                    file=geojson_template_file_path, mode="r", encoding="utf-8"
                ) as geojson_file:
                    geojson = json.load(geojson_file, strict=False)

                    # Load statistics
                    with open(source_file_path, "r") as csv_file:
                        csv_statistics = pd.read_csv(csv_file, dtype=str)

                        # Iterate over features
                        for feature in sorted(
                            geojson["features"],
                            key=lambda feature: feature["properties"]["id"],
                        ):
                            # Build statistics structure
                            if (
                                feature["properties"]["id"]
                                not in json_statistics[year][half_year]
                            ):
                                json_statistics[year][half_year][
                                    feature["properties"]["id"]
                                ] = {}

                            # Filter statistics
                            statistic_filtered = csv_statistics[
                                csv_statistics["id"].astype(str)
                                == str(feature["properties"]["id"])
                            ]

                            # Iterate over attributes
                            for attribute in input_port.attributes:
                                if not statistic_filtered[attribute].empty:

                                    # Read value and convert to float or int respectively
                                    value = statistic_filtered[attribute].iloc[0]
                                    value = (
                                        float(value)
                                        if "." in str(value)
                                        else int(value)
                                    )

                                    feature["properties"][f"{attribute}"] = value
                                    json_statistics[year][half_year][
                                        feature["properties"]["id"]
                                    ][attribute] = value

                        if clean or not os.path.exists(target_file_path):
                            os.makedirs(
                                os.path.dirname(target_file_path), exist_ok=True
                            )
                            with open(
                                target_file_path, "w", encoding="utf-8"
                            ) as geojson_file:
                                json.dump(geojson, geojson_file, ensure_ascii=False)
                                converted += 1

                                not quiet and print(
                                    f"✓ Convert {os.path.basename(target_file_path)}"
                                )
                        else:
                            already_exists += 1
                            not quiet and print(
                                f"✓ Already exists {os.path.basename(statistics_file_path)}"
                            )
                            continue
            except Exception as e:
                exception += 1
                not quiet and print(f"✗️ Exception: {str(e)}")

        if clean or not os.path.exists(statistics_file_path):
            os.makedirs(os.path.dirname(statistics_file_path), exist_ok=True)
            with open(statistics_file_path, "w", encoding="utf-8") as json_file:
                json.dump(json_statistics, json_file, ensure_ascii=False)
                converted += 1
                not quiet and print(
                    f"✓ Aggregate statistics {os.path.basename(statistics_file_path)}"
                )
        else:
            already_exists += 1
            not quiet and print(
                f"✓ Already exists {os.path.basename(statistics_file_path)}"
            )

    print(
        f"blend_data finished with already_exists: {already_exists}, converted: {converted}, exception: {exception}"
    )
